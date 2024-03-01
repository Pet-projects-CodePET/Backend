from rest_framework import serializers

from apps.profile.models import Profile


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.avatar = validated_data.get("avatar", instance.avatar)
        instance.nickname = validated_data.get("nickname", instance.nickname)
        instance.name = validated_data.get("name", instance.name)
        instance.about = validated_data.get("about", instance.about)
        instance.portfolio = validated_data.get(
            "portfolio", instance.portfolio
        )
        instance.contacts = validated_data.get("contacts", instance.contacts)
        instance.birthday = validated_data.get("birthday", instance.birthday)
        instance.specialization = validated_data.get(
            "specialization", instance.specialization
        )
        instance.skill = validated_data.get("skill", instance.skill)
        instance.level = validated_data.get("level", instance.level)
        instance.ready_to_participate = validated_data(
            "ready_to_participate", instance.ready_to_participate
        )
        instance.save()
        return instance
