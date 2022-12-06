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

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipes")
    ingredients = models.ManyToManyField(Ingredient, related_name="recipes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")

    class Meta:
        ordering = ['title']


    def __str__(self):
        return self.title

