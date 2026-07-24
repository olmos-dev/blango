from rest_framework import generics

from blog.api.serializers import PostSerializer
from blog.models import Post


class PostList(generics.ListCreateAPIView):
    print("Ejecutando GET en PostList")
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    print("Ejecutando GET en PostList")
    queryset = Post.objects.all()
    serializer_class = PostSerializer