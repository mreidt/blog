from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    """List every blog posts"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
