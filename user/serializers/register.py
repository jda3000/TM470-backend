from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password_repeat']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def validate_password_repeat(self, value):
        if self.initial_data['password'] != value:
            raise serializers.ValidationError('Passwords do not match')
        return value

    def create(self, validated_data):
        # remove repeat password for saving
        del validated_data['password_repeat']

        user = get_user_model()(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user
