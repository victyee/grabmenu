from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from restaurants import views
from home import views
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, RestaurantsViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'restaurants': RestaurantsViewSitemap,
}

urlpatterns = patterns('',

    url(r'^batcave/', include(admin.site.urls)),

    #homepage
    url(r'^$', 'home.views.home', name='home'),

    #all restaurants
    url(r'^all/$', 'restaurants.views.all', name='all_restaurants'),

    #search
    url(r'^s/$', 'restaurants.views.search', name='search'),
   
    #contact us
    url(r'^contact/$', 'contact.views.contact', name='contact'),

    # owners page
    url(r'^owners/$', 'owners.views.owners', name='owners'),

    #nav pages
    url(r'^about/$', 'home.views.about', name='about'),
    url(r'^faq/$', 'home.views.faq', name='faq'),
    url(r'^terms/$', 'home.views.terms', name='terms'),

    #sitemaps
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    #restaurant page views
    url(r'^(?P<slug>[\w-]+)/$', 'restaurants.views.single', name='single_restaurant'),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)


if settings.DEBUG:
    handler404 = 'home.views.custom_404'
    handler500 = 'home.views.custom_500'
