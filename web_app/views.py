from django.shortcuts import render
from .models import Audio
from django.core.mail import send_mail
from django.conf import settings


# HOME PAGE

def homepage(request):

    query = request.GET.get('q', '')

    if query:
        songs = Audio.objects.filter(name__icontains=query)
    else:
        songs = Audio.objects.all()

    return render(request,'homepage.html',
        {
            'songs': songs,
            'query': query
        }
    )


# AUDIOS PAGE

def audios(request):

    songs = Audio.objects.all()

    return render(request,'audios.html',
        {
            'songs': songs
        }
    )


# ABOUT PAGE

def about(request):

    return render(request,'about.html')


def contact(request):
   return render(request,'contact.html')