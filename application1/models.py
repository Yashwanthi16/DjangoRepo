from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 100) 
    image = models.ImageField(upload_to= "images/")
    video = models.FileField(upload_to= "media/", default = "")
    description = models.TextField()
    author = models.CharField(max_length = 100)
    created_at = models.DateTimeField(default = datetime.now)
    
    #to print object as string: but in admin UI this will be like displaying the title 
    def __str__(self):
        return self.title