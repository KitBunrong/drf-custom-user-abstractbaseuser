from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/profile/", include("apps.profiles.urls")),
]

admin.site.site_header = "Custom Model"
admin.site.site_title = "Custom Model Admin"
admin.site.index_title = "Welcome to Custom Model Example"
