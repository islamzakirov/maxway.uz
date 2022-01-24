from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import BaseAuthentication
from rest_framework import filters
# from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class BurgerViewSet(viewsets.ModelViewSet):
    queryset = Burger.objects.all()
    serializer_class = BurgerSerializer
    filterset_field = ['name', 'content']
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name', 'price']
    ordering = ['name']
    search_fields = ['name']
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class BurgerNumberPaginations(PageNumberPagination):
#     page_size = 3

class CardItemViewSet(viewsets.ModelViewSet):
    queryset = CardItem.objects.all()
    serializer_class = CardItemSerializer        
    permission_classes = [IsAuthenticated]

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]