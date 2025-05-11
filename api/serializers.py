from rest_framework import serializers
from data.models import User, News, Complaint, Profile, Gallery, Report, LetterRecap
import os

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role']


class NewsSerializer(serializers.ModelSerializer):
    poster = UserSerializer(read_only=True)
    class Meta:
        model = News
        # fields = ['id', 'poster', 'title', 'content', 'created_at']
        fields = '__all__'


class GetNewsSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id','slug', 'title', 'content', 'poster', 'thumbnail_url', 'created_at']

    def get_thumbnail_url(self, obj):
        request = self.context.get('request')
        if obj.thumbnail:
            return request.build_absolute_uri(obj.thumbnail.url)
        return None

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['id', 'user', 'content', 'status', 'created_at']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"
        
    def validate_pdf(self, value):
        if not value.name.lower().endswith('.pdf'):
            raise serializers.ValidationError("Only PDF files are allowed.")
        return value
    
class LetterRecapSerializer(serializers.ModelSerializer):
    class Meta:
        model = LetterRecap
        fields = "__all__"