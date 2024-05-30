from django.shortcuts import render, redirect
from about.models import *
from .forms import FormContact, FormSubscribers


# Create your views here.

def contact(request, redirected=False):
    if request.method == 'POST':
        return redirect('/success/', redirected=True)
    me = Me.objects.get(name='Umarjon')
    context = {
        'me': me,
        'social_media': me.social_media.all(),
        'redirected': redirected
    }
    return render(request, 'contact.html', context)


def success(request):
    me = Me.objects.get(name='Umarjon')
    form1 = FormSubscribers(request.POST or None)
    form = FormContact(request.POST or None)
    if form.is_valid():
        form.save()
    if form1.is_valid():
        form1.save()
    context = {
        'social_media': me.social_media.all(),
    }
    return render(request, 'success.html', context)
