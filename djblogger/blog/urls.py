from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage.as_view(), name='home'),
    path('<slug:post>/', views.post_single, name='post-single')
]
