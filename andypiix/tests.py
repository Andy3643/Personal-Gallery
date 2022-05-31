from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Image,Location,Category

class ImageTest(TestCase):
    '''
    Test  Image class
    '''
    def setUp(self):
        '''
        Sets up the tests
        '''
        
        self.new_location = Location(location='kericho')
        self.new_location.save()
        self.new_category = Category(category='Cars')
        self.new_category.save()
        self.new_image = Image(image='media/Kerichocar.jpeg',img_name='My car',img_description='this is my car',img_location=self.new_location,img_category=self.new_category)
        self.new_image.save()

    def tearDown(self):
        '''
        clears the database after every test
        '''
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        
        
        
    def test_delete_method(self):
        '''
        Test delete function
        '''
        self.new_image.delete_image()
        saved_images = Image.objects.all()
        self.assertTrue(len(saved_images)==0)