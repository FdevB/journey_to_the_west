from django.urls import path

from accounts_app import views


app_name = 'accounts_app'
urlpatterns = [
    path('sign-up/', views.signup_view, name='sign-up'),
    path('log-in/', views.login_view, name='log-in'),
    path('log-out/', views.logout_view, name='log-out'),
]
