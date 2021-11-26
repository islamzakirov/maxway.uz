from django.db.models import fields
from rest_framework import serializers
from .models import *

class BurgerSerializer(serializers.ModelSerializer):
    class Meta():
        model = Burger
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = '__all__'

