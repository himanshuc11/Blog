from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'username']

    def save(self):
        email = self.validated_data['email']
        password = self.validated_data['password']
        username = self.validated_data['username']
        User.objects.create_user(username=username, email=email, password=password)

class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
