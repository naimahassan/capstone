from django.shortcuts import render
from django.http import HttpResponse
from . models import Post,Profile 
import datetime as dt 
from django.contrib.auth.models import User
from . forms import NewPostForm

# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request, 'index.html',{"post":post})

def post(request):
    post = Post.get_post()
    return render(request, 'all-cakey/post.html',{"post":post})

def detail(request,post_id):
    post = Post.objects.get(id = post_id)
    print(post)
    return render(request, 'all-cakey/detail.html',{"post":post})           

def profile(request,user_id):
    current_user = request.user
    profile = Profile.objects.all()
    post = Post.objects.filter(profile__id=user_id)

    return render(request, 'all-cakey/profile.html', {"current_user":current_user,"profile":profile,"post":post}) 


def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect ('post')
    else:
        form = NewPostForm()
    return render(request, 'all-cakey/new-post.html', {"form":form})       

       


