from rest_framework import generics, serializers

from apps.profile.models import Profile, UserSkill


class ProfileUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Profile
        fields = "__all__"

    def to_representation(self, instance):
        user = self.context["request"].user
        visibile_status = instance.visible_choices

        representation = {}

        if user.is_authenticated:
            if visibile_status == "all":
                representation["email"] = instance.email
                representation["telegram"] = instance.telegram
                representation["phone_number"] = instance.phone_number
            elif visibile_status == "only_creator" and instance.user == user:
                representation["email"] = instance.email
                representation["telegram"] = instance.telegram
                representation["phone_number"] = instance.phone_number
            else:
                representation["message"] = "Недоступно"
        else:
            representation["message"] = "Недоступно"

        return representation


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
