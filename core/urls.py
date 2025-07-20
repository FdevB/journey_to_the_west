"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('blog/', include('blog_app.urls')),
    path('about-us/', include('about_app.urls')),
    path('contact-us/', include('contact_app.urls')),

    # Library
    path('ckeditor/', include('django_ckeditor_5.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
