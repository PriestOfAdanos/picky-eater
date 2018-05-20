from django.contrib import admin
from .models import Friendship, Ingredient, Recipe

admin.site.register(Friendship)
admin.site.register(Ingredient)
admin.site.register(Recipe)

