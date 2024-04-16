"""
URL configuration for recipeapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipe_list'),
    path('<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    path('<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
]
