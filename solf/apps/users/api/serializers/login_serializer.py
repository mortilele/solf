from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, write_only=True, required=True)
    password = serializers.CharField(max_length=128, write_only=True, required=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        validated_data = super().validate(data)
        username = validated_data['username']
        password = validated_data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        validated_data['token'] = user.token
        return validated_data
