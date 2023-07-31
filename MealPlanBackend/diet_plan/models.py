from django.db import models

class Recipe(models.Model):
    recipeName = models.CharField(max_length=100)
    calories = models.IntegerField()
    estimatedTime = models.IntegerField()

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields for ingredient details.

class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe)
    # Add other fields for meal plan details.
