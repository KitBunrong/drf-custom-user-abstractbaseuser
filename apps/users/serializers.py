from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="profile.gender")
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMetaField()
    full_name = serializers.SerializerMethodField(source="get_full_name")

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "gender",
        ]

    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_last_name(self, obj):
        return obj.last_name.title()


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
        ]
