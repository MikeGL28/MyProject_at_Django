from django.shortcuts import render
from .models import Certificate

def programming_page(request):
    certificates = Certificate.objects.all().order_by('-created_at')
    resume_url = "/media/resume/Mikhail_Gavrilov_resume.pdf"  # например
    return render(request, 'index.html', {
        'certificates': certificates,
        'resume_url': resume_url
    })