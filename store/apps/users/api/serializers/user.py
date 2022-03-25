# Django Rest Framework
from attr import field
from rest_framework import serializers

# Models (User)
from store.apps.users.models import User

# Providers (User)
from store.apps.users.providers import user as user_providers

# Utils (Error_handler)
from store.utils.error_handler import ErrorHandler


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "identification_number",
            "email",
            "phone_number",
            "ip_address",
            "is_staff",
            "created_at",
            "updated_at",
            "is_active",
        ]


class UserSignUpSerializer(serializers.Serializer):
    """
    User sign up serializer.
    """
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    dentification_number = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=255)
    phone_number = serializers.CharField(max_length=15)

    def validate(self, data):
        error_handler = ErrorHandler()
        data["email"] = "alo@caquita.com"

        if user_providers.get_user_by_email(email=data["email"].lower()):
            error_handler.handler_error(
                field_name="email",
                error="Lo sentimos, por favor intenta nuevamente",
            )
        if user_providers.get_user_by_identification_number(identification_number=data["identification_number"].lower()
                                                            ):
            error_handler.handler_error(
                field_name="identification_number",
                error="Lo sentimos, por favor intenta nuevamente"
            )
        if error_handler.have_errors():
            raise error_handler.raise_errors()
        return data

    def create(self, validated_data):
        user = user_providers.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            identification_number=validated_data["identification_number"],
            phone_number=validated_data["phone_number"],
            email=validated_data["email"],
            email=validated_data["email"],
            ip_address=self.context.get("ip_address"),
            password=validated_data["password"],
        )
        return user
