from rest_framework import serializers
from .models import Meal, Rating

class MealSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Meal
        fields = ('id', 'title', 'description', ) 


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        #fileds = '__all__'
        fields = ('id', 'stars', 'user', 'meal')
        #depth = 3