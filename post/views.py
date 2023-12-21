from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm




def home(request):
    if request.method == 'GET':
        posts = Post.objects.all().order_by('-id')
        return render(request, 'post/post_list.html', {'posts': posts})



def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(title=data['title'], image=data['image'], description=data['description'])
            messages.success(request, 'پست با موفقیت ایجاد شد')
            return redirect('post:home')
    elif not request.user.is_superuser:
        return redirect('post:home')
    else:
        form = PostForm()
    
    return render(request, 'post/create_post.html', {'form': form})

