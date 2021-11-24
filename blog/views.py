from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from blog.models import Blog
from blog.serializers import BlogSerializer, CommentSerializer


class BlogAPIListView(ListAPIView):
    """
    Create blog api_view
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogAPICreateView(CreateAPIView):

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #

    def create(self, request, *args, **kwargs):
        serialized_blog = BlogSerializer(
            context={"request": request}, data=request.data
        )
        serialized_blog.is_valid(raise_exception=True)
        serialized_blog.save()

        return Response(
            {
                "data": serialized_blog.data,
                "message": "Blog created successfully!",
            },
            status=status.HTTP_201_CREATED,
        )


class CommentAPIView(CreateAPIView):
    """
    Create comment api_view
    """
    def create(self, request, *args, **kwargs):
        serialized_comment = CommentSerializer(
            context={"request": request}, data=request.data
        )
        serialized_comment.is_valid(raise_exception=True)
        serialized_comment.save()

        return Response(
            {
                "data": serialized_comment.data,
                "message": "Comment created successfully!",
            },
            status=status.HTTP_201_CREATED,
        )

