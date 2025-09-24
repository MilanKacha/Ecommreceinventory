from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        error_messages={"required": "Please provide email"}
    )
    password = serializers.CharField(
        write_only=True,
        error_messages={"required": "Please provide password"}
    )

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid email or password")

        if user.account_status != 'Active':
            raise serializers.ValidationError("Your account is not active")

        data['user'] = user
        return data



