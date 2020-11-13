from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.flowers = Category(name='Flowers')

    def test_instance(self):
        self.assertTrue(isinstance(self.flowers,Category)) 

    def test_save_method(self):
        self.flowers.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)   