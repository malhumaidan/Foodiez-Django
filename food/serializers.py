from rest_framework import serializers
from .models import Category, Recipe, Ingredient





####################################### Category ##############################################

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "id", "image"]



####################################### Recipe ##############################################


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ["title", "body", "image", "category", "ingredients", "user", "inputingerdients", "id"]
        # depth = 1 (yousef changes)


    # def create(self, validated_data):
    #     validated_data['user'] = self.context.get('request').user
    #     validated_data['category'] = Category.objects.get(id=validated_data['category'])
    #     print(validated_data['category'])
    #     return super().create(validated_data) (yousef changesgit )

####################################### Ingredient ##############################################
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["body"]