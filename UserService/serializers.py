from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Users



class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)
    confirm_password = serializers.CharField(write_only=True, required=True, min_length=6)

    class Meta:
        model = Users
        fields = ['email', 'username', 'password', 'confirm_password', 'profile_pic']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Password and Confirm Password do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password
        password = validated_data.pop('password')
        user = Users(**validated_data)
        user.set_password(password)
        user.save()
        return user

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



