from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.ImageField(upload_to = 'photos/')
    image_name=models.CharField(max_length =60)
    image_description=models.TextField()
    image_location=models.ForeignKey('Location',on_delete=models.CASCADE)
    image_category=models.ForeignKey('Category',on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    @classmethod
    def get_images(cls):
        all_images = cls.objects.all()
        return all_images

    @classmethod
    def filter_by_location(cls,id):
        image_by_location = cls.objects.filter(image_location_id = id)  
        return image_by_location

    @classmethod
    def search_image(cls,category):
        photos = cls.objects.filter(image_category__name__icontains=category) 
        return photos      

class Location(models.Model):
    name = models.CharField(max_length = 60)

    def save_location(self):
        self.save()

class Category(models.Model):
    name = models.CharField(max_length = 60)

    def save_category(self):
        self.save()
