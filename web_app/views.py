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
    success = None

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New Contact Form Message from {name}"

        email_message = f"""
Name: {name}
Email: {email}

Message:
{message}
"""

        try:
            send_mail(
                subject,
                email_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],  # receives email in your Gmail
                fail_silently=False,
            )

            success = "Message sent successfully!"

        except Exception as e:
            success = f"Error sending message: {e}"

    return render(request, "contact.html", {"success": success})