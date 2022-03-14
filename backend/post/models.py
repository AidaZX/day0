from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=100)
    file_type =  models.CharField(max_length=100)
    size =  models.CharField(max_length=100)
    file = models.FileField(upload_to='post_files')
    
    def __str__(self):
        return self.name