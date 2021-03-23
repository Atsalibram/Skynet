from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.
class LocationTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.test_location = Location(location="Greece")

    def test_instance(self):
        self.assertTrue(isinstance(self.test_location,Location))
    
    def test_save_location(self):
        self.test_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.test = Category(category="Travel")

    def test_instance(self):
        self.assertTrue(isinstance(self.test,Image))

    def test_save_category(self):
        self.test.save_category()












        
        images =  Category.objects.all()
        self.assertTrue(len(images)>0)