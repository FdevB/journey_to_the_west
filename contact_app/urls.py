from django.urls import path

from contact_app import views


app_name = 'contact_app'
urlpatterns = [
    path('', views.contact_view, name='contact-us'),
]
