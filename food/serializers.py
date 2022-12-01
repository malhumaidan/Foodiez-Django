from rest_framework import serializers
from .models import Category, Recipe, Ingredient





####################################### Category ##############################################

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "id"]



####################################### Recipe ##############################################


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["title", "body", "image"]






####################################### Ingredient ##############################################
