from django.shortcuts import render, get_object_or_404

from .models import Hobby


def hobby_list(request):
    hobbies = Hobby.objects.all()
    return render(request, 'hobby/list.html', {'hobbies': hobbies})


def hobby_detail(request, slug):
    hobby = get_object_or_404(Hobby, slug=slug)
    return render(request, 'hobby/detail.html', {'hobby': hobby})