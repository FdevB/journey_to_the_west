from django.urls import path

from blog_app import views


app_name = 'blog_app'
urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('category/<slug:category_name>', views.blog_view, name='blog-category'),
    path('tag/<slug:tag_name>', views.blog_view, name='blog-tag'),
    path('author/<str:author_name>', views.blog_view, name='blog-author'),
    path('detail/<slug:slug>/', views.blog_detail_view, name='blog-detail'),
]
