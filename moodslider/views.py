from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'moodslider/index.html')

def upload(request):
    return render(request, 'moodslider/upload.html')
