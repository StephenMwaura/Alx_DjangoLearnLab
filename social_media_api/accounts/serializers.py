from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','bio', 'profile_picture','followers')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','bio', 'profile_picture','followers')
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()