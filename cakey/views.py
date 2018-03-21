from django.shortcuts import render
from django.http import HttpResponse
from . models import Post,Profile,Recipe
import datetime as dt 
from django.contrib.auth.models import User
from . forms import NewRecipeForm

# Create your views here.
def index(request):
    recipe = Recipe.get_recipe()
    post = Post.objects.all()
    return render(request, 'index.html',{"recipe":recipe,"post":post})

def post(request):
    post = Post.get_post()
    return render(request, 'all-cakey/post.html',{"post":post})

def recipe(request):
    recipe = Recipe.objects.all()
    if request.method == 'POST':
        form = NewRecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect ('recipe')
    else:
        form = NewRecipeForm()
    return render(request, 'all-cakey/recipe.html',{"recipe":recipe})            
