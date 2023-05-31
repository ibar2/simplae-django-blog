from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage.as_view(), name='home'),
    path('search/', views.search.as_view(), name='search'),
    path('<slug:post>/', views.post_single, name='post-single'),
    path('tag/<slug:tag>', views.taglist.as_view(), name='tag-list')
]
