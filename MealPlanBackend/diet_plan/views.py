from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Recipe, Ingredient, MealPlan
from .serializers import RecipeSerializer, IngredientSerializer, MealPlanSerializer

@api_view(['GET'])
def list_meal_plans(request):
    meal_plans = MealPlan.objects.all()
    serializer = MealPlanSerializer(meal_plans, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_meal_plan(request, meal_plan_id):
    try:
        meal_plan = MealPlan.objects.get(pk=meal_plan_id)
    except MealPlan.DoesNotExist:
        return Response({"error": "Meal Plan not found."}, status=404)

    serializer = MealPlanSerializer(meal_plan)
    return Response(serializer.data)

@api_view(['POST'])
def create_meal_plan(request):
    serializer = MealPlanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_meal_plan(request, meal_plan_id):
    try:
        meal_plan = MealPlan.objects.get(pk=meal_plan_id)
    except MealPlan.DoesNotExist:
        return Response({"error": "Meal Plan not found."}, status=404)

    serializer = MealPlanSerializer(meal_plan, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_meal_plan(request, meal_plan_id):
    try:
        meal_plan = MealPlan.objects.get(pk=meal_plan_id)
    except MealPlan.DoesNotExist:
        return Response({"error": "Meal Plan not found."}, status=404)

    meal_plan.delete()
    return Response({"message": "Meal Plan deleted successfully."}, status=204)
