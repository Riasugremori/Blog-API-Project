from rest_framework import viewsets
from .models import Author, Blog
from .serializers import AuthorModelSerializer, BlogModelSerializer

class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
