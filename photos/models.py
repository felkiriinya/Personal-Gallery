from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.ImageField(upload_to = 'photos/')
    image_name=models.CharField(max_length =60)
    image_description=models.TextField()
    image_location=models.ForeignKey('Location',on_delete=models.CASCADE)
    image_category=models.ForeignKey('Category',on_delete=models.CASCADE)

