from django.shortcuts import render
from .models import GuitarSong

def guitar_page(request):
    songs = GuitarSong.objects.all().order_by('title')
    return render(request, 'guitar/index.html', {'songs': songs})