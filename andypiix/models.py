from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Image(models.Model):
    """
    create an image model
    """
    image = models.ImageField(upload_to='andypiix/')
    img_name = models.CharField(max_length=40)
    img_description = models.TextField()
    img_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    img_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.image_name
    

class Category(models.Model):
    '''
    create a  Category model
    '''
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category
    
class Location(models.Model):
    '''
    create location model
    '''
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location