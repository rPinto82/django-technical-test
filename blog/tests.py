import json

from rest_framework.test import APITestCase
from model_bakery import baker

from blog.models import Blog


class TestBlog(APITestCase):

    def setUp(self):
        blogs = baker.make("blog.Blog", _quantity=10)
        baker.make("blog.Comment", blog=blogs[0], _quantity=10)

    def test_blog(self):
        """
        Add test for blog
        """
        response = self.client.get("/api/blog/list/")

        self.assertEqual(response.status_code, 200, "Status code is not 200")

        blog_list = len(json.loads(response.content))

        self.assertEqual(blog_list, 10, "Expecting 10 blogs but found %s" % blog_list)

    def test_comment(self):
        """
        Add test for comment
        """
        response = self.client.post("/api/comment/create/", data={"blog": 1, "text": "this is a test"})

        # check if the status is 200
        self.assertEqual(response.status_code, 201, "Status code is not 201")
