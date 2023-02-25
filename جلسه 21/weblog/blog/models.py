from django.db import models


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


class Comment(models.Model):
    author = models.CharField(max_length=50)
    author_email = models.EmailField()
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post: {self.post}\nCommenter: {self.author}"
