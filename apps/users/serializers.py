from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="profile.gender")

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "gender",
        ]

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(
            instance
        )
        if instance.is_superuser:
            representation["admin"] = True
        return representation


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        ]
