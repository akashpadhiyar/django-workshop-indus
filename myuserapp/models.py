from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField()
    email = models.EmailField(blank=False)
    address = models.CharField()
    
    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.title

      