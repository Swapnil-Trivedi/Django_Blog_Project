from cgi import test
import imp
from multiprocessing import AuthenticationError
from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #create a user
        testUser1=User.objects.create_user(username="testUser1",password='abc123#')
        testUser1.save()

        #create a blog post
        testPost=Post.objects.create(author=testUser1,title="Blog title", body="dummy text")
        testPost.save()
    
    def testBlogData(self):
        post=Post.objects.get(id=1)
        author=f'{post.author}'
        title=f'{post.title}'
        body=f'{post.body}'
        self.assertEqual(author,'testUser1')
        self.assertEqual(title,'Blog title')
        self.assertEqual(body,"dummy text")
