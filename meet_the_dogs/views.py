from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def meet_the_dogs(request):
    """
    View function that renders the 'home.html' template.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTTP response using the 'home.html' template.
    """
    template = loader.get_template('home.html') #user 'home.html' template
    return HttpResponse(template.render())
