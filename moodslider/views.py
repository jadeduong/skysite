from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return render(request, 'moodslider/index.html')

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save("programmedata.xml", uploaded_file)
        return render(request, 'moodslider/index.html')
    return render(request, 'moodslider/upload.html')
