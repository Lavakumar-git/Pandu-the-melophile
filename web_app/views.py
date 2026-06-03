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


# CONTACT PAGE




def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            subject=f"New Contact Message from {name}",
            message=f"""
Name: {name}

Email: {email}

Message:
{message}
""",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return render(
            request,
            "contact.html",
            {"success": "Message sent successfully!"}
        )

    return render(request, "contact.html")