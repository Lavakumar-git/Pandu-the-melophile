from django.shortcuts import render
from .models import Audio


def homepage(request):
    query = request.GET.get('q', '')

    if query:
        songs = Audio.objects.filter(name__icontains=query)
    else:
        songs = Audio.objects.all().order_by('-uploaded_at')

    latest_songs = Audio.objects.all().order_by('-uploaded_at')[:8]

    categories = Audio.objects.values_list(
        'category',
        flat=True
    ).distinct()

    context = {
        'songs': songs,
        'query': query,
        'latest_songs': latest_songs,
        'categories': categories,
    }

    return render(request, 'homepage.html', context)


def audios(request):
    category = request.GET.get('category')

    if category:
        songs = Audio.objects.filter(
            category__iexact=category
        ).order_by('-uploaded_at')
    else:
        songs = Audio.objects.all().order_by('-uploaded_at')

    categories = Audio.objects.values_list(
        'category',
        flat=True
    ).distinct()

    context = {
        'songs': songs,
        'categories': categories,
        'selected_category': category,
    }

    return render(request, 'audios.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')