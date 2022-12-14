from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(blank=True)


    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.TextField()



    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField()
    inputingerdients = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipes")
    ingredients = models.ManyToManyField(Ingredient, related_name="recipes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")



    def __str__(self):
        return self.title

