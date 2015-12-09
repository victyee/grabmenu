from django.contrib import admin
# Register your models here.
from .models import Restaurant, MenuTitle, MenuItem


class MenuTitleInline(admin.StackedInline):
    model = MenuTitle
    extra = 0

class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 0

class RestaurantAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("restaurant_name",)}
	search_fields = ["restaurant_name"]
	ordering = ["restaurant_name"]
	class Meta:
		model = Restaurant

	inlines = [MenuTitleInline]

admin.site.register(Restaurant, RestaurantAdmin)


class MenuTitleAdmin(admin.ModelAdmin):
	list_display = ["restaurant", "mealtype", "number"]
	list_editable = ["number", "mealtype"]
	search_fields = ["title"]
	ordering = ["restaurant", "number"]
	class Meta:
		model = MenuTitle
	inlines = [MenuItemInline]

admin.site.register(MenuTitle, MenuTitleAdmin)

