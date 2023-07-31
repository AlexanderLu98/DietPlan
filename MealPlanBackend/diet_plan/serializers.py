from rest_framework import serializers
from .models import Recipe, Ingredient, MealPlan

# diet_plan/serializers.py

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'  # Include all fields of the Recipe model

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'  # Include all fields of the Ingredient model

class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = '__all__'  # Include all fields of the MealPlan model
