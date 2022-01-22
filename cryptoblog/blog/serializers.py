from rest_framework import serializers
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.user', read_only=True)
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Post
        fields = '__all__'
