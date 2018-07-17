from rest_framework import viewsets, mixins
from post.models import Post
from post.serializers import PostSerializer


class PostViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

