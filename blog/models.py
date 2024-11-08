from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images')
    create_at = models.DateField()
    description = models.TextField()
    
    def __str__(self):
        return self.title