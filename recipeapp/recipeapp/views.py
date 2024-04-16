from django.views import View
from django.shortcuts import render
from recipes.models import Recipe

class HomeView(View):
    def get(self, request):
        # Get the count of recipes
        recipe_count = Recipe.objects.count()

        # Get all recipe objects
        recipes = Recipe.objects.all()

        # Create the context dictionary
        context = {
            'recipe_count': recipe_count,
            'recipes': recipes
        }

        # Render the template with the context
        return render(request, 'recipeapp/home.html', context)