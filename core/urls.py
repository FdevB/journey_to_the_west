"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from debug_toolbar.toolbar import debug_toolbar_urls

from core import settings
from home_app.sitemaps import HomeSitemap
from blog_app.sitemaps import BlogSitemap, PostSitemap, CategorySitemap, TagSitemap
from info_app.sitemaps import InfoSitemap


sitemaps = {
    'home': HomeSitemap,
    'blog': BlogSitemap,
    'posts': PostSitemap,
    'categories': CategorySitemap,
    'tags': TagSitemap,
    'informations': InfoSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('blog/', include('blog_app.urls')),
    path('info/', include('info_app.urls')),
    path('accounts/', include('accounts_app.urls')),

    # Library
    path('ckeditor/', include('django_ckeditor_5.urls')),

    # SiteMap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # Robots.txt
    path('robots.txt', include('robots.urls'))
] 

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
