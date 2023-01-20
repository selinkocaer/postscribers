from django.shortcuts import render, redirect
from .models import PostModel
from .forms import PostModelForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')
    else:
        form = PostModelForm()
    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'blog/index.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)
