from ast import Delete
from distutils.command.upload import upload
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
#CRUD
class Category(models.Model):
    '''
    create a  Category model
    '''
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category
    
    
    def save_category(self):
        """
        add new category to database
        """
        self.save()
        
    def update_category(self):
        """
        edit existing category in database
        """
        pass
    
    def delete_category(self):
        """
        delete existing category from the database
        """
        self.delete()
        
class Location(models.Model):
    '''
    create location model
    '''
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location
    
    def save_location(self):
        """
        save new location to database
        """
        self.save()
    
    def update_location(self):
        """
        edit location saaved in the database
        """
        pass
    
    def Delete_location(self):
        """
        delete location from the database
        """
        self.delete()
class Image(models.Model):
    """
    create an image model
    """
    image = CloudinaryField('image')
    img_name = models.CharField(max_length=40)
    img_description = models.TextField()
    img_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    img_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.img_name
    
    def add_image(self):
        """
        add new image to database storage
        """
        self.save()
        
    def update_image(self):
        """
        replace a certain image in the database
        """
        pass
    
    def delete_image(self):
        """
        Remove image from database
        """
        self.delete()
        
    @classmethod
    def get_all_images(cls):
        """
        get all images from database
        """
        return cls.objects.all()

    @classmethod
    def search_image_by_id(cls):
        """
        search image using id
        """ 
        found_image = cls.objects.filter(pk = id)
        return found_image
    
    @classmethod
    def search_image_by_category(cls,searched_category):
        '''
        filter the images by category
        '''
        found_image = cls.objects.filter(image_category__category__icontains=searched_category)
        return found_image

    @classmethod
    def search_by_location(cls,location):
        '''
        filter images by their location
        '''
        found_image = cls.objects.filter(image_location__location__icontains=location)
        return found_image

    

# class Tag(models.Model):
#     '''
#     image tag class
#     '''
#     name = models.CharField(max_length=30) 

#     def __str__(self):
#         return self.name
