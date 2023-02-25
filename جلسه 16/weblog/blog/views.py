from django.shortcuts import render, redirect

from .models import Post

def post_list_view(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(status='pub')
    context = { 'posts': posts }
    return render(request, 'blog/posts_list.html', context)

def post_detail_view(request, pk):
    from django.shortcuts import get_object_or_404
    post = get_object_or_404(Post, pk=pk)
    context = { 'post': post }
    return render(request, 'blog/post_detail.html', context)

def post_create_view(request):
    from .forms import PostForm
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', { 'form': form } )


    # from django.contrib.auth.models import User
    # if request.method=='POST':
    #     title = request.POST['title']
    #     text = request.POST.get('text')
    #     user = User.objects.first()
    #     Post.objects.create(title=title, text=text, status='pub', author=user)
    # return render(request, 'blog/new_post.html')


