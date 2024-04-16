from django.shortcuts import render
from django.views import View
from recipes.models import Recipe

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {
            'recipes': Recipe.objects.all(),
            'recipe_count':  Recipe.objects.count()
        })