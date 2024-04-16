from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListView.as_view(), name='list_recipe'),
    path('create/', views.CreateRecipe.as_view(), name='create_recipe'),
    path('<int:recipe_id>/', views.DetailRecipe.as_view(), name='detail_recipe'),
    path('<int:recipe_id>/update/', views.UpdateRecipe.as_view(), name='update_recipe'),
    path('<int:recipe_id>/delete/', views.DeleteRecipe.as_view(), name='delete_recipe'),
]