from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework import generics
from django.shortcuts import render


# Create your views here.

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
