from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.list_recipes),
    path('recipes/create/', views.create_recipe),
    path('recipes/<int:recipe_id>/', views.get_recipe),
    path('recipes/<int:recipe_id>/update/', views.update_recipe),
    path('recipes/<int:recipe_id>/delete/', views.delete_recipe),

    path('ingredients/', views.list_ingredients),
    path('ingredients/create/', views.create_ingredient),
    path('ingredients/<int:ingredient_id>/', views.get_ingredient),
    path('ingredients/<int:ingredient_id>/update/', views.update_ingredient),
    path('ingredients/<int:ingredient_id>/delete/', views.delete_ingredient),

    path('mealplans/', views.list_meal_plans),
    path('mealplans/create/', views.create_meal_plan),
    path('mealplans/<int:meal_plan_id>/', views.get_meal_plan),
    path('mealplans/<int:meal_plan_id>/update/', views.update_meal_plan),
    path('mealplans/<int:meal_plan_id>/delete/', views.delete_meal_plan),
]
