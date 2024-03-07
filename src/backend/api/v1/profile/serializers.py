from rest_framework import serializers

from apps.profile.models import Profile


class ProfileUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Profile
        fields = "__all__"
