from recipes.models import Food, Recipe, Ingredient
from recipes.forms import IngredientForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

class FoodListView(ListView):
    model = Food

class FoodDetailView(DetailView):
    model = Food

class FoodCreateView(CreateView):
    model = Food

class RecipeListView(ListView):
    model = Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render_to_response('recipes/recipe_list.html', {'object_list': recipes}, context_instance=RequestContext(request))

class RecipeDetailView(DetailView):
    model = Recipe

class RecipeCreateView(CreateView):
    model = Recipe

class RecipeUpdateView(UpdateView):
    model = Recipe

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm

    def get_initial(self, *args, **kwargs):
        recipe = Recipe.objects.get(slug=self.kwargs['slug'])
        return {'recipe': recipe}

    def get_success_url(self):
        return reverse('recipe-detail', args=[self.kwargs['slug']])

class IngredientDeleteView(DeleteView):
    model = Ingredient

    def get_success_url(self):
        return reverse('recipe-detail', args=[self.kwargs['slug']])
