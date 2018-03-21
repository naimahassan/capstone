from django.shortcuts import render
from django.http import HttpResponse
from . models import Post,Profile,Cake
import datetime as dt 
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    cake = Cake.get_cake()
    post = Post.objects.all()
    return render(request, 'index.html',{"cake":cake,"post":post})

def post(request):
    post = Post.get_post()
    return render(request, 'all-cake/post.html',{"post":post})
