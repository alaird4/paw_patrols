from django.urls import path
from . import views

urlpatterns = [
    path('', views.meet_the_dogs, name='meet_the_dogs'), #URL specific for dogs application
]
