from rest_framework import serializers
from .models import Post
from users.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'user', 'content', 'created_at', 'updated_at', 'comment_count')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_comment_count(self, obj):
        return obj.comments.count() 