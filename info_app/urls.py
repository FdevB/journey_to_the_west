from django.urls import path

from info_app import views


app_name = 'info_app'
urlpatterns = [
    path('about-us', views.about_view, name='about-us'),
    path('contact-us', views.contact_view, name='contact-us'),
]
