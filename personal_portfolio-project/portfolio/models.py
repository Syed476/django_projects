from django.db import models

# Create your models here.

class Project (models.Model):
    title=models.CharField(max_length=10)
    description=models.CharField(max_length=120)
    images=models.ImageField(upload_to='portfolio/images')
    url=models.URLField(blank=True)
