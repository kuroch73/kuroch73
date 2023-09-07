from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)              # Строка с огр знаками
    desc = models.CharField(max_length=150)              # Строка с огр знаками
    image = models.ImageField(upload_to='blog/image/')   # Строка под изоброжение
    date = models.DateField()                            # Дата
    url = models.URLField()                              # Ссылка