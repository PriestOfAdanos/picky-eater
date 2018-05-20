from django.urls import path
from . import views

urlpatterns = [
    path('user-profile/', views.my_profile, name='user_profile'),
    path('home/', views.home, name='home')
]
