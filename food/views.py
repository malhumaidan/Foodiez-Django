from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializer
from .models import Category

# Create your views here.

####################################### Category ##############################################

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreate(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated]


class CategoryThreeInOne(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"
    lookup_url_kwarg = "object_id"


####################################### Recipe ##############################################
