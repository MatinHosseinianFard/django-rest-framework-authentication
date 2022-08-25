from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializers


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    lookup_field = "slug"