from rest_framework import serializers

from users.models import User
from users.tasks import create_user


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "phone", "verify_status")


class UserCreateSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data):
        tenant_name = validated_data.pop("organization_name") if validated_data.get("organization_name") else None
        instance = super().create(validated_data)
        instance.set_password(validated_data["password"])
        instance.save()
        create_user(instance.id, tenant_name)
        return instance

    class Meta:
        model = User
        fields = "__all__"
