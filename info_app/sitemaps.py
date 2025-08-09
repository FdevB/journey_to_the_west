from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class InfoSitemap(Sitemap):
    """
    Generates sitemap entries for about-us and contact-us page.

    Attributes:
        changefreq (str): The expected frequency of changes. Here set to "yearly", meaning the content is updated regularly.
        priority (float): The relative importance of this page compared to other pages. 0.5 indicates medium importance.

    Methods:
        items(): Returns a list of static view names to include in the sitemap.
        location(item): Resolves and returns the absolute URL for each static view.
    """

    changefreq = 'yearly'
    priority = 0.5

    def items(self):
        return ['info_app:contact-us', 'info_app:about-us']
    
    def location(self, obj):
        return reverse(obj)
