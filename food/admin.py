from django.contrib import admin

from food.models import Category, Ingredient, Recipe

# Register your models here.
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Ingredient)
