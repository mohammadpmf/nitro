from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    author = models.CharField(max_length=100, verbose_name='نویسنده')
    description = models.TextField(verbose_name='توضیحات')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='قیمت')
    cover = models.ImageField(upload_to="covers/", verbose_name='عکس جلد', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])

from django.contrib.auth import get_user_model

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.text}"
