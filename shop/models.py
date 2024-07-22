from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    description = models.TextField(max_length=200)
    product = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='shop/pictures/', null=True)
    price = models.FloatField(default=0)
    quantity= models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Cart(models.Model):
    product_name=models.CharField(max_length=200)
    price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    total=models.PositiveIntegerField(default=0)



class Client(models.Model):
    full_name=models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    profession=models.CharField(max_length=200)



