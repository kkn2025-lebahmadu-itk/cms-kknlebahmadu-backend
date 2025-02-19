from rest_framework import serializers
from data.models import User, News
import os

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role']


class NewsSerializer(serializers.ModelSerializer):
    poster = UserSerializer(read_only=True)
    class Meta:
        model = News
        fields = ['id', 'poster', 'title', 'content', 'created_at']