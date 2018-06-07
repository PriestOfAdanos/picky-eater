from django.db import models
from picky_eater.settings import AUTH_USER_MODEL
from django.utils.timezone import now
from custom_users.models import Restaurant


class Friendship(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(AUTH_USER_MODEL, related_name="friendship_creator_set", on_delete='cascade')
    friend = models.ForeignKey(AUTH_USER_MODEL, related_name="friend_set", on_delete='cascade')


class Ingredient(models.Model):  # make it more efficient                                  #todo
    name = models.CharField(max_length=100)
    alternative_names = models.ManyToManyField('self', null=True, blank=True, default=None)

    def __str__(self):
        return self.name # study what happens to alternative names and relations when particular ingriedient gets deleted


class Recipe(models.Model):
    owner = models.OneToOneField(Restaurant, on_delete='cascade', related_name='menu_position')
    name = models.CharField(max_length=100)
    ingredients = models.ForeignKey(Ingredient, on_delete='cascade')
    published = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


class ListedIngredient(models.Model):  # Creates a relation between the user and a Ingredient
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete='cascade')
    ingredient = models.ForeignKey(Ingredient, on_delete='protect')  # todo
    is_blackist = models.BooleanField(default=True)  # if true, user needs to avoid it
    is_greylist = models.BooleanField(default=True)   # if true, user wants avoid it
    is_greenlist = models.BooleanField(default=False)  # if true, user wants to eat it more
# Default values are set like this for safety reasons( there is always a of us sending a vegan user to hamburger shop)
