from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog_app.models import PostModel, CategoryModel, TagModel


class BlogSitemap(Sitemap):
    """
    Generates sitemap entries for blog's home page.

    Attributes:
        changefreq (str): The expected frequency of changes. Here set to "daily", meaning the content is updated regularly.
        priority (float): The relative importance of this page compared to other pages. 1.0 indicates the highest possible importance.

    Methods:
        items(): Returns a list of static view names to include in the sitemap.
        location(item): Resolves and returns the absolute URL for each static view.
    """

    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return ['blog_app:blog']
    
    def location(self, obj):
        return reverse(obj)


class PostSitemap(Sitemap):
    """
    Generates sitemap entries for all published blog posts.

    Attributes:
        changefreq (str): The expected frequency of changes. Here set to "weekly", meaning the content is updated frequently.
        priority (float): The relative importance of this page compared to other pages. 0.9 indicates high importance.

    Methods:
        items(): Returns all posts with status set to "published".
        lastmod(obj): Returns the last modified datetime for each post, helping search engines know when to re-crawl it.
    """

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return PostModel.objects.filter(status='published')
    
    def lastmod(self, obj):
        return obj.updated_at


class CategorySitemap(Sitemap):
    """
    Generates sitemap entries for all blog categories.

    Attributes:
        changefreq (str): The expected frequency of changes. Here set to "monthly", meaning updates are less frequent.
        priority (float): The relative importance of this page compared to other pages. 0.7 indicates medium-high importance.

    Methods:
        items(): Returns all categories available in the blog.
    """

    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return CategoryModel.objects.all()


class TagSitemap(Sitemap):
    """
    Generates sitemap entries for all blog tags.

    Attributes:
        changefreq (str): The expected frequency of changes. Here set to "monthly", as tags are less likely to change often.
        priority (float): The relative importance of this page compared to other pages. 0.7 indicates medium-high importance.

    Methods:
        items(): Returns all tags available in the blog.
    """
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return TagModel.objects.all()
