from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


# Create your views here.
def index(request):
    msg = 'My Message'
    return render(request, 'index.html', {'message': msg})

def rank(request):
    return render(request, 'rank.html')

def search(request):
    return render(request, 'search.html')

def community(request):
    return render(request, 'community.html')

def error(request):
    raise Http404("Not Found")
