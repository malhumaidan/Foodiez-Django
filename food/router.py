from food.views import  CategoryViewSet, IngredientViewSet, RecipeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"recipes", RecipeViewSet, basename="recipe"),
router.register(r"ingredients", IngredientViewSet, basename="ingredient"),
