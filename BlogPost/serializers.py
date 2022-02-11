import imp
from rest_framework import serializers
from .models import Post
from BlogUser.serializers import ListUserSerializer

class ListSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='email', read_only=True)
    # owner = ListUserSerializer(read_only=True)
    class Meta:
        model = Post
        exclude = ['id']

class PostCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['id']