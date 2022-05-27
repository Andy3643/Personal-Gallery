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
    