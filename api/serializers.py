from rest_framework import serializers
from .models import User,BlogModel,CommentModel

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields='__all__'

class BlogSerializer(serializers.ModelSerializer):
    username=serializers.CharField(source="user.username")
    class Meta:
        model=BlogModel
        fields="__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentModel
        fields="__all__"