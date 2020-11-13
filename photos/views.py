from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404

# Create your views here.

def photos(request):
    return render(request, 'all-photos/all_photos.html')