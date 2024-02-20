from django.urls import path

from .views import post_list, post_detail, author_detail
urlpatterns = [
    
    path('posts', post_list),
    path('<int:pk>/', post_detail),
    path('authors/<int:pk>/', author_detail),
]
