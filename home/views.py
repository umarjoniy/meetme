from django.shortcuts import render
from about.models import *


# Create your views here.
def index(request):
    me = Me.objects.get(name='Umarjon')
    context = {
        'me': me,
        'social_media': me.social_media.all(),
        'skills': me.technologies.all().order_by('-percent'),
        'cv': me.cv,
        'experiences': me.experience.all().order_by('id'),
        'educations': me.education.all().order_by('id'),
        'statistics': me.statistics.all(),
        'projects': me.projects.all()
    }
    return render(request, 'index.html', context)


def blog(request):
    me = Me.objects.get(name='Umarjon')
    context = {
        'social_media': me.social_media.all(),
    }
    return render(request, 'blog.html', context)


def portfolio(request):
    me = Me.objects.get(name='Umarjon')
    context = {
        'social_media': me.social_media.all(),
        'projects': me.projects.all()
    }
    return render(request, 'portfolio.html', context)


def projects(request, slug):
    me = Me.objects.get(name='Umarjon')
    context = {
        'social_media': me.social_media.all(),
        'project': me.projects.get(slug=slug)
    }
    return render(request, 'project.html', context)
