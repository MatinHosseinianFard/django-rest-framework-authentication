from django.urls import path

from .views import ArticleList, ArticleDetail, UserList, UserDetail

app_name = "api"

urlpatterns = [
    path("articles/", ArticleList.as_view(), name="article-list"),
    path("articles/<slug:slug>/", ArticleDetail.as_view(), name="article-detail"),
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user-detail"),
]
