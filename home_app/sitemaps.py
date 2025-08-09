from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class HomeSitemap(Sitemap):
    """
    Generates sitemap entries for home page.

    Attributes:
        changefreq (str): The expected frequency of changes. Here set to "yearly", meaning the content is updated regularly.
        priority (float): The relative importance of this page compared to other pages. 1.0 indicates the highest possible importance.

    Methods:
        items(): Returns a list of static view names to include in the sitemap.
        location(item): Resolves and returns the absolute URL for each static view.
    """

    changefreq = 'yearly'
    priority = 1

    def items(self):
        return ['home_app:home']
    
    def location(self, obj):
        return reverse(obj)
