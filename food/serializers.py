from rest_framework import serializers
from .models import Category, Ingredients, Recipe, Ingredient





####################################### Category ##############################################

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "id", "image"]



####################################### Recipe ##############################################


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["title", "body", "image", "category", "ingredients", "user"]


####################################### Ingredient ##############################################
class IngredientsSercializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ["body"]