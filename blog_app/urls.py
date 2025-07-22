from django.urls import path

from blog_app import views


app_name = 'blog_app'
urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('detail/<slug:slug>/', views.blog_detail_view, name='blog-detail'),
]
