from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from .models import Recipe

# Create your views here.
class CreateRecipe(CreateView):
    model = Recipe
    fields = ['title', 'description', 'ingredients', 'instructions', 'image']
    template_name = 'recipes/create_recipe.html'
    success_url = '/'

class DeleteRecipe(DeleteView):
    model = Recipe
    template_name = 'recipes/delete_recipe.html'
    success_url = '/'

class UpdateRecipe(UpdateView):
    model = Recipe
    fields = ['title', 'description', 'ingredients', 'instructions', 'image']
    template_name = 'recipes/update_recipe.html'
    success_url = '/'

class ListRecipe(ListView):
    model = Recipe
    template_name = 'recipes/list_recipe.html'
    context_object_name = 'recipes'

class DetailRecipe(DetailView):
    model = Recipe
    template_name = 'recipes/detail_recipe.html'
    context_object_name = 'recipe'