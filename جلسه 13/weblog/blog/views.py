from django.shortcuts import render

from .models import Post

def post_list_view(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(status='pub')
    context = { 'posts': posts }
    return render(request, 'blog/posts_list.html', context)

# def post_detail_view(request, pk):
#     from django.http import HttpResponse
#     return HttpResponse(f"pk: {pk}")

# def post_detail_view(request, pk):
#     post = Post.objects.get(pk=pk)
#     context = { 'post': post }
#     return render(request, 'blog/post_detail.html', context)

# # Error Handling 1    
# def post_detail_view(request, pk):
#     try:
#         post = Post.objects.get(pk=pk)
#         context = { 'post': post }
#         return render(request, 'blog/post_detail.html', context)
#     except Post.DoesNotExist:
#         return render(request, 'blog/post_detail.html', { 'post' : None })

# # Error Handling 2
# def post_detail_view(request, pk):
#     from django.core.exceptions import ObjectDoesNotExist
#     try:
#         post = Post.objects.get(pk=pk)
#         context = { 'post': post }
#         return render(request, 'blog/post_detail.html', context)
#     except ObjectDoesNotExist:
#         return render(request, 'blog/post_detail.html', { 'post' : None })

def post_detail_view(request, pk):
    from django.shortcuts import get_object_or_404
    post = get_object_or_404(Post, pk=pk)
    context = { 'post': post }
    return render(request, 'blog/post_detail.html', context)



