from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from dj_rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path("", include("blog.urls")),
    path("api/", include("api.urls")),
    path("admin/", admin.site.urls),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    re_path(
        r'^account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(template_name="api/account_confirm_email.html"),
        name='account_confirm_email',
    ),
    path('api/dj-rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
