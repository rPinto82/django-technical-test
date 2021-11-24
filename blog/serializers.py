from rest_framework import serializers

from blog.models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Create comment serializer
    """
    class Meta:
        model = Comment
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    """
    Create blog serializer
    """

    class Meta:
        model = Blog
        fields = '__all__'

