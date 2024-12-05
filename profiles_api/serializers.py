from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ("id", "name", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data.get("email"),
            name=validated_data.get("name"),
            password=validated_data.get("password"),
        )
        return user

    def update(self, instance, validated_data):
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)
        return super().update(instance, validated_data)


class ProfileFeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfileFeed
        fields = ("id", "user", "content", "created_on")
        extra_kwargs = {"user": {"read_only": True}}
