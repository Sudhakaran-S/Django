from django.db import models

# Create your models here.
class rewrite(models.Model):
    # id: int
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics') 
    desc = models.TextField()
    review = models.IntegerField()
    price = models.IntegerField()
    rate = models.BooleanField(default=False)

class Categories(models.Model):
    # id: int
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics') 