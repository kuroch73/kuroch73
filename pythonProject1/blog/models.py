from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=150)
    image = models.ImageField(upload_to='blog/image/')
    date = models.DateField()
    url = models.URLField()