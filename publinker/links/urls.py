from django.urls import path

from .views import homepage, redirect_


urlpatterns = [path("", homepage), path("<str:key>/", redirect_)]
