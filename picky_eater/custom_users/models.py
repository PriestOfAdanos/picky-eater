from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager, Group, Permission
from django.utils import timezone


class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """My custom user model, instead of username it uses email"""
    email = models.EmailField(unique=True, null=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """"
        Returns the short name for the user.
        """
        return self.first_name


class Restaurant(AbstractBaseUser, PermissionsMixin):
    """Model representing a restaurant. Unlike a normal user,
    it has values that allow me to differentiate legit business from scam(NIP, location)"""
    email = models.EmailField(unique=True, null=True)
    objects = BaseUserManager()
    NIP = models.IntegerField()
    restaurant_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('Restaurants_group'),
        blank=True,
        help_text=_(
            'You can pointout that you belong to some restaurant groups(Pizza hut, KFC and so on...)'
        ),
        related_name="restaurants_set",
        related_query_name="restaurant",
        default=None
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="restaurant_set",
        related_query_name="restaurant",
    )
    USERNAME_FIELD = 'email'

    def recipe(self):
        self.recipe = self.Recipe()
        self.ingredients = self.Recipe.ingredients








