from django.conf.urls import patterns, url

from recipes.views import FoodListView, FoodDetailView, FoodCreateView
from recipes.views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView
from recipes.views import IngredientCreateView, IngredientDeleteView
from recipes.views import recipe_list

urlpatterns = patterns('',
                       url(r'^food/$', FoodListView.as_view(), name='food-list'),
                       url(r'^food/(?P<pk>\d+)/$', FoodDetailView.as_view(), name='food-detail'),
                       url(r'^food/new/', FoodCreateView.as_view(), name='food-create'),
                       url(r'^$', recipe_list, name='recipe-list'),
                       url(r'^new/$', RecipeCreateView.as_view(), name='recipe-create'),
                       url(r'^(?P<slug>[-\w]+)/$', RecipeDetailView.as_view(), name='recipe-detail'),
                       url(r'^(?P<slug>[-\w]+)/edit/$', RecipeUpdateView.as_view(), name='recipe-update'),
                       url(r'^(?P<slug>[-\w]+)/add_ingredient/$', IngredientCreateView.as_view(), name='ingredient-create'),
                       url(r'^(?P<slug>[-\w]+)/remove_ingredient/(?P<pk>\d+)/$', IngredientDeleteView.as_view(), name='ingredient-delete'),
                       )
