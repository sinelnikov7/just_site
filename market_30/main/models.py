from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=250)
    discription = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_created=True)
    update = models.DateTimeField(auto_now=True)
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title








# Create your models here.
