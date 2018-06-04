from django.urls import path
from . import views

urlpatterns = [
    path(r'^signup/$', views.user_signup, name='signup'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.user_activate, name='activate'),
]