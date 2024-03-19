from rest_framework import generics, serializers

from apps.profile.models import Profile, UserSkill
from apps.projects.models import Project


class ProfileUpdateSerializer(serializers.ModelSerializer):
    """Модель сериализатора профиля с учетом выбора видимости контактов"""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Profile
        fields = [
            "avatar",
            "name",
            "about",
            "portfolio_link",
            "birthday",
            "country",
            "city",
            "specialization",
            "skill",
            "level",
            "ready_to_participate",
        ]

    def to_representation(self, instance):
        user = self.context["request"].user
        visible_status_contacts = instance.visible_status_contacts

        if user.is_authenticated:
            if (
                visible_status_contacts == 2
                and Project.objects.filter(creator=user).exists()
            ):
                return super().to_representation(instance)
            if visible_status_contacts == 3:
                self.fields.pop("phone_number")
                self.fields.pop("email")
                self.fields.pop("telegram")
                return super().to_representation(instance)
        return {}


class UserSkillSerializer(serializers.ModelSerializer):
    skills = serializers.PrimaryKeyRelatedField(
        queryset=UserSkill.objects.all(), many=True
    )

    class Meta:
        model = Profile
        fields = ["user", "skill"]
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Profile.objects.all(),
                fields=["user", "skill"],
                message="Этот навык вами уже был выбран",
            )
        ]
