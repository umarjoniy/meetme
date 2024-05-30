from django.shortcuts import render
from .models import *


def about(request):
    me = Me.objects.get(name='Umarjon')

    context = {
        'me': me,
        'social_media': me.social_media.all(),
        'skills': me.technologies.all().order_by('-percent'),
        'cv': CV.objects.get(id=me.cv.id),
        'statistics': me.statistics.all()
    }

    return render(request, 'about_me.html', context=context)
# Create your views here.
