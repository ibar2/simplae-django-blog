from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage.as_view(), name='home')
]
