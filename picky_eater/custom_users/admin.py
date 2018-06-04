from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Restaurant
from interactions.models import Recipe, Ingredient, Friendship, ListedIngredient

admin.site.register(get_user_model())
admin.site.register(Recipe)
admin.site.register(Restaurant)
admin.site.register(Ingredient)
admin.site.register(Friendship)
admin.site.register(ListedIngredient)