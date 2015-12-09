from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings

# Create your models here.

STATE_CHOICES = (
	('Victoria', 'Victoria'),
	('New South Wales', 'New South Wales'),
	('South Australia', 'South Australia'),
	('Queensland', 'Queensland'),
	('Western Australia', 'Western Australia'),
	('Australian Capital Territory', 'Australian Capital Territory'),
	('Northern Territory', 'Northern Territory'),
	('Tasmania', 'Tasmania'),
	)

MEAL_TYPE = (
	('1Entrees', 'Entrees'),
	('2Sides', 'Sides'),
	('3Mains', 'Mains'),
	('4Drinks', 'Drinks'),
	('5Desserts', 'Desserts'),
	('6Specials', 'Specials'),
	('7Others', 'Others'),
	('8Lunch', 'Lunch'),
	)

class Restaurant(models.Model):
	user = models.CharField(max_length=250, default='grabmenu')
	restaurant_name = models.CharField(max_length=250)
	restaurant_address1 = models.CharField(max_length=250)
	restaurant_address2 = models.CharField(max_length=250)
	restaurant_state = models.CharField(max_length=120, choices=STATE_CHOICES)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['restaurant_name']

	def __unicode__(self):
		return self.restaurant_name

	def get_absolute_url(self):
		return reverse("single_restaurant", kwargs={"slug": self.slug})


class MenuTitle(models.Model):
	restaurant = models.ForeignKey(Restaurant)
	title = models.CharField(max_length=120, null=True, blank=True)
	description = models.TextField(max_length=1000, null=True, blank=True)
	mealtype = models.CharField(max_length=120, choices=MEAL_TYPE)
	number = models.IntegerField(default=1, null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['mealtype', 'number']

	def __unicode__(self):
		return self.mealtype


class MenuItem(models.Model):
	title = models.ForeignKey(MenuTitle)
	item_name = models.CharField(max_length=200)
	description = models.TextField(max_length=1000, null=True, blank=True)
	price = models.CharField(max_length=20, null=True, blank=True)
	number = models.IntegerField(default=1, null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['number']

	def __unicode__(self):
		return self.item_name