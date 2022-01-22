from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from .models import Post
from .serializers import (
    PostListSerializer,
)


class CreatPostAPIView(CreateAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self, *args, **kwargs):
        # queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Post.objects.all()
        return queryset_list


class PostDetailAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = PostListSerializer

    def get_queryset(self):
        id = self.kwargs.get('pk')
        queryset = Post.objects.filter(id=id)

        return queryset
