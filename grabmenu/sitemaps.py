from django.contrib import sitemaps
from django.core.urlresolvers import reverse

from restaurants.models import Restaurant

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'all_restaurants', 'search', 'contact', 'owners', 'about',\
        'faq', 'terms']

    def location(self, item):
        return reverse(item)


class RestaurantsViewSitemap(sitemaps.Sitemap):
	changefreq = 'daily'
	priority = 1.0

	def items(self):
		return Restaurant.objects.all()