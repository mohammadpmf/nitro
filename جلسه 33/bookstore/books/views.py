from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Book

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    template_name = "books/book_list.html"
    context_object_name = "books"


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"


def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all()
    from .forms import CommentForm
    if request.method=="POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, "books/book_detail.html", {
        'book': book,
        'comments': comments,
        'comment_form': comment_form,
        })


class BookCreateView(generic.CreateView):
    model = Book
    template_name = "books/book_create.html"
    fields = ["title", "author", "description", "price", "cover"]
    success_url = reverse_lazy("book_list")

class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = "books/book_update.html"
    fields = ["title", "author", "description", "price", "cover"]

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("book_list")

