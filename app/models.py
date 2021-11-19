from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = CloudinaryField('image')
    demo = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title