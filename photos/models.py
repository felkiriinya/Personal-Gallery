from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField

import cloudinary


class Image(models.Model):
    
    image=CloudinaryField('image')
    image_name=models.CharField(max_length =60)
    image_description=models.TextField()
    image_location=models.ForeignKey('Location',on_delete=models.CASCADE)
    image_category=models.ForeignKey('Category',on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_images(cls):
        all_images = cls.objects.all()
        return all_images

    @classmethod
    def filter_by_location(cls,id):
        image_by_location = cls.objects.filter(image_location_id = id)  
        return image_by_location

    @classmethod
    def filter_by_category(cls,id):
        image_by_category = cls.objects.filter(image_category_id = id)  
        return image_by_category

    @classmethod
    def search_image(cls,category):
        photos = cls.objects.filter(image_category__name__icontains=category) 
        return photos      

class Location(models.Model):
    name = models.CharField(max_length = 60)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

class Category(models.Model):
    name = models.CharField(max_length = 60)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()
