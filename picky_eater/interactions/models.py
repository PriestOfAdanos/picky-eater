from django.db import models
from django.utils.timezone import now
from picky_eater.settings import AUTH_USER_MODEL


class Ingredient(models.Model):   # make it more efficient                                  #todo
    name = models.CharField(max_length=100)
    alternative_names = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ForeignKey(Ingredient)
    published = models.DateTimeField(default=now)

    def __str__(self):
        return self.name
    # photo =                                                                               #todo


class Friendship(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(AUTH_USER_MODEL, related_name="friendship_creator_set")
    friend = models.ForeignKey(AUTH_USER_MODEL, related_name="friend_set")
