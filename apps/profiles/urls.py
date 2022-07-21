from django.urls import path

from .views import GetProfileAPIView

urlpatterns = [path("me/", GetProfileAPIView.as_view(), name="get_profile")]
