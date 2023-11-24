from django.urls import path
from .views import index, post_detail, category_posts

app_name = 'blog'  # Пространство имен для приложения blog

urlpatterns = [
    path('', index, name='index'),  # Домашняя страница
    path('posts/<int:id>/', post_detail, name='post_detail'),  # Детали поста
    path('category/<slug:category_slug>/', category_posts,
         name='category_posts'),  # Посты в категории
]
