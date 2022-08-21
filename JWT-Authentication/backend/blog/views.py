from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Article


class ArticleList(ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = "articles"


class ArticleDetail(DetailView):
    template_name = "blog/article_detail.html"
    context_object_name = "article"

    def get_object(self):
        return get_object_or_404(
            Article.objects.filter(status=True),
            pk=self.kwargs["pk"])
