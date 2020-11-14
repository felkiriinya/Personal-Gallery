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

class LocationTestClass(TestCase):
    def setUp(self):
        self.nairobi = Location(name='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location)) 

    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)    

class ImageTestClass(TestCase):
    def setUp(self):
        self.flowers = Category(name = 'Flowers')
        self.flowers.save_category()

        self.locations = Location(name='Nairobi')
        self.locations.save_location()

        self.new_image=Image(image_name='rose',image_description='A beautiful flower',image_category=self.flowers,image_location=self.locations)
        self.new_image.save_image()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_get_images(self):
        all_images = Image.get_images()
        self.assertTrue(len(all_images)>0)

    def test_filter_by_location(self):
        test_location_id = 6
        images_location = Image.filter_by_location(test_location_id) 
        self.assertTrue(len(images_location) == 0)  

    def test_filter_by_category(self):
        test_category_id = 6
        images_category = Image.filter_by_category(test_category_id) 
        self.assertTrue(len(images_category) == 0)       

    def test_delete_image(self):
        self.new_image.save_image()
        image1 = Image.objects.all()
        self.assertEqual(len(image1),1)
        self.new_image.delete_image()
        image2 = Image.objects.all()
        self.assertEqual(len(image2),0)    