from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Post

class MyTestsForWeblog(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="user1")
        self.post1 = Post.objects.create(
            title = 'Post 1',
            text = "This is the first post of weblog.",
            status = Post.STATUS_CHOICES[0][0], # published
            author = self.user
        )
        
    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_is_post_title_in_blog_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
    
    def test_post_detail_url(self):
        # response = self.client.get('/blog/1/')
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_are_post_title_and_text_in_blog_details(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)
    
    def test_get_404(self):
        response = self.client.get(reverse('post_detail', args=[99]))
        self.assertEqual(response.status_code, 404)



