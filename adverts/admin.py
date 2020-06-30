from django.contrib import admin
from .models import Category, Advert, Location, Option, Item_condition





class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Location, LocationAdmin)

class OptionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Option, OptionAdmin)

class Item_conditionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Item_condition, Item_conditionAdmin)




class AdvertAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'id', 'item_condition', 'location', 'option','available', 'pub_date', 'updated_at']
    list_filter = ['available', 'pub_date', 'updated_at']
    list_editable = ['price', 'item_condition', 'option',  'location', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Advert, AdvertAdmin)





