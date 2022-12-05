from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CategorySerializer, RecipeSerializer
from .models import Category, Recipe
from rest_framework import viewsets

# Create your views here.

####################################### Category ##############################################

# class CategoryList(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class CategoryCreate(CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsAuthenticated]


# class CategoryThreeInOne(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = "id"
#     lookup_url_kwarg = "object_id"


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):

        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]



####################################### Recipe ##############################################

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all ()
    serializer_class = RecipeSerializer

    def get_permissions(self):

        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]






