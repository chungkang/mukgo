from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


# Create your views here.
def index(request):
    msg = 'My Message'
    return render(request, 'index.html', {'message': msg})


def error(request):
    raise Http404("Not Found")
