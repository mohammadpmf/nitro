from django.db import models
from django.urls import reverse
# from django.shortcuts import reverse # یا از اینجا هم میشه ایمپورت کرد.

class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'published'),
        ('drf', 'draft'),
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    # یا این طوری
    # def get_absolute_url(self):
    #     return reverse("post_detail", args=[self.pk])

    # یا این طوری
    # def get_absolute_url(self):
    #     return reverse("post_detail", args=[self.id])

    # یا این طوری
    # def get_absolute_url(self):
    #     return reverse("post_detail", kwargs={"pk": self.id})
