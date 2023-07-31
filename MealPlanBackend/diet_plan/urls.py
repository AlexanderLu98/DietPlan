from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('diet_plan.urls')),

    path('api/recipes/', views.list_recipes),
    path('api/recipes/<int:recipe_id>/', views.get_recipe),
    path('api/recipes/create/', views.create_recipe),
    path('api/recipes/<int:recipe_id>/update/', views.update_recipe),
    path('api/recipes/<int:recipe_id>/delete/', views.delete_recipe),

    path('api/ingredients/', views.list_ingredients),
    path('api/ingredients/<int:ingredient_id>/', views.get_ingredient),
    path('api/ingredients/create/', views.create_ingredient),
    path('api/ingredients/<int:ingredient_id>/update/', views.update_ingredient),
    path('api/ingredients/<int:ingredient_id>/delete/', views.delete_ingredient),

    path('api/mealplans/', views.list_meal_plans),
    path('api/mealplans/<int:meal_plan_id>/', views.get_meal_plan),
    path('api/mealplans/create/', views.create_meal_plan),
    path('api/mealplans/<int:meal_plan_id>/update/', views.update_meal_plan),
    path('api/mealplans/<int:meal_plan_id>/delete/', views.delete_meal_plan),
]
