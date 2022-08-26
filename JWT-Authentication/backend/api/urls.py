from django.urls import path

from .views import ArticleList, ArticleDetail, UserList, UserDetail

app_name = "api"

urlpatterns = [
    path("article/", ArticleList.as_view(), name="article-list"),
    path("article/<int:pk>/", ArticleDetail.as_view(), name="article-detail"),
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user-detail"),
]
