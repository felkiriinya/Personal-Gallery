from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image,Location,Category

# Create your views here.

def photos(request):
    images = Image.get_images()
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'all-photos/all_photos.html',{"images":images,"locations":locations,"categories":categories})

def photos_by_location(request, location_id):
    images = Image.filter_by_location(location_id) 
    return render(request,'all-photos/location.html',{"images":images}) 

def photos_by_category(request, category_id):
    images = Image.filter_by_category(category_id) 
    return render(request,'all-photos/category.html',{"images":images}) 

def search_images(request):

    if 'photo' in request.GET and request.GET["photo"]:
        category= request.GET.get("photo")
        searched_images = Image.search_image(category)
        message = f"{category}"

        return render(request, 'all-photos/search.html',{"message":message, "photos":searched_images})

    else:
        message = "You have not searched for any picture"
        return render(request, 'all-photos/search.html',{"message":message})   