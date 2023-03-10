from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .forms import PostForm
from .models import Post

def post_list_view(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(status='pub').order_by('-datetime_modified')
    context = { 'posts': posts }
    return render(request, 'blog/posts_list.html', context)

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = { 'post': post }
    return render(request, 'blog/post_detail.html', context)

def post_create_view(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', { 'form': form })


# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('posts_list')
#     return render(request, 'blog/new_post.html', { 'form': form })

def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request, 'blog/new_post.html', { 'form': form })
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            # return redirect('post_detail',pk=pk)
            return redirect('posts_list')

def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('posts_list')