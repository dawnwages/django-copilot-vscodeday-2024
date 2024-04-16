from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Recipe

# Create your views here.
# Detail View
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

# List View
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

# Create View
class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'recipes/recipe_create.html'
    fields = '__all__'
    success_url = '/recipes/'

# Update View
class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'recipes/recipe_update.html'
    fields = '__all__'
    success_url = '/recipes/'

# Delete View
class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_delete.html'
    success_url = '/recipes/'