from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def meet_the_dogs(request):
    template = loader.get_template('home.html') #user 'home.html' template
    return HttpResponse(template.render())
