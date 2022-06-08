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
        testUser2=User.objects.create_user(username="testUser2",password="abc123")
        testUser2.save()
        #create a blog post
        testPost=Post.objects.create(author=testUser1,title="Blog title", body="dummy text")
        testPost.save()
        testPost2=Post.objects.create(author=testUser2,title="dum dum",body="random")
        testPost2.save()
    
    def testUser1(self):
        post=Post.objects.get(id=1)
        author=f'{post.author}'
        title=f'{post.title}'
        body=f'{post.body}'
        self.assertEqual(author,'testUser1')
        self.assertEqual(title,'Blog title')
        self.assertEqual(body,"dummy text")

    def testUser2(self):
        post1=Post.objects.get(id=2)
        author1=f'{post1.author}'
        title1=f'{post1.title}'
        body1=f'{post1.body}'
        self.assertEqual(author1,'testUser2')
        self.assertEqual(title1,'dum dum')
        self.assertEqual(body1,"random")
