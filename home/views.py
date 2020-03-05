from django.shortcuts import render
from django.http import Http404
from .models import Channel


def index(request):
    msg = 'My Message'
    return render(request, 'index.html', {'message': msg})


def rank(request):
    channels = Channel.objects.filter(published_at__isnull=False).filter().order_by('-published_at')
    return render(request, 'rank.html', {'channels': channels})


def category_rank(request, category):
    channels = Channel.objects.filter(published_at__isnull=False).order_by('-published_at')
    return render(request, 'rank.html', {'channels': channels, 'category': category})


def community(request):
    return render(request, 'community.html')


def error(request):
    raise Http404("Not Found")
