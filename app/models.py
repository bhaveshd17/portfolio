from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='images/')
    demo = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title