from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=250)
    discription = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_created=True)
    update = models.DateTimeField(auto_now=True)
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Magazin(models.Model):
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    products = models.ManyToManyField('Product')

    def __str__(self):
        return self.name


class TimeOpen(models.Model):
    time_open = models.TimeField(help_text="Время работы")
    time_close = models.TimeField(help_text="Время работы")
    name = models.OneToOneField(Magazin, on_delete=models.DO_NOTHING)

    def __str__(self):

        return f"Время работы {self.name}"

# Create your models here.
