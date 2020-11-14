from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image,Location,Category
# Create your views here.

def photos(request):
    images = Image.get_images()
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'all-photos/all_photos.html',{"images":images,"locations":locations,"categories":categories})