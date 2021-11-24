from django.urls import path
from blog.views import BlogAPIListView, BlogAPICreateView, CommentAPIView

app_name = "blog"

urlpatterns = [
    path('blog/list/', BlogAPIListView.as_view()),
    path('blog/create/', BlogAPICreateView.as_view()),
    path('comment/create/', CommentAPIView.as_view())
]
