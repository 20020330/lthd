from django.contrib.auth.forms import UserCreationForm
from django.db.models.base import Model as Model
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post
from .forms import *

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')  # Điều hướng người dùng sau khi đăng ký thành công đến trang đăng nhập
    else:
        form = UserCreationForm()
    return render(request, 'democrud/register.html', {'form': form})


class PostIndexView(generic.ListView):
    template_name = 'democrud/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # get queryset of posts  
        return Post.objects.all()

def read_post(request, id):
    # Retrieve the post from the database
    post = get_object_or_404(Post, pk=id)
    # Render the template with the post data
    return render(request, 'democrud/post/read.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/post') 
    else:
        form = PostForm()
    return render(request, 'democrud/post/create.html', {'form': form})

def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return render(request, 'democrud/post/read.html', {'post': post})
    else:
        form = PostForm(instance=post)
    return render(request, 'democrud/post/update.html', {'form': form})
    
def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        post.delete()
        return redirect('/post')  
    return render(request, 'democrud/post/read.html', {'post': post})