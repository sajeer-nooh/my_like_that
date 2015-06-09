from rest_framework import serializers
from django.contrib.auth.models import User
from app_user.models import AppUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class AppUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = AppUser