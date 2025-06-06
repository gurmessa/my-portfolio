from django.test import TestCase
from django.urls import reverse
from blogs.models import Blog


class BlogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 10 blog posts for pagination tests
        number_of_blogs = 10
        for blog_id in range(number_of_blogs):
            Blog.objects.create(
                title=f"Blog {blog_id}",
                content=f"This is the content of blog {blog_id}",
                status=Blog.StatusChoices.PUBLISHED,
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/blogs/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("blogs:blog_list"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("blogs:blog_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogs/blog_list.html")

    def test_pagination_is_ten(self):
        response = self.client.get(reverse("blogs:blog_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] == False)
        self.assertEqual(len(response.context["blogs"]), 10)


class BlogDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a blog post for detail view tests
        Blog.objects.create(
            title="Test Blog",
            slug="test-blog",
            content="This is the content of the test blog",
            published_date="2023-01-01",
            status=Blog.StatusChoices.PUBLISHED,
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/blogs/test-blog/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        blog = Blog.objects.get(slug="test-blog")
        response = self.client.get(reverse("blogs:blog_detail", args=[blog.slug]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        blog = Blog.objects.get(slug="test-blog")
        response = self.client.get(reverse("blogs:blog_detail", args=[blog.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogs/blog_detail.html")

    def test_view_uses_correct_context(self):
        blog = Blog.objects.get(slug="test-blog")
        response = self.client.get(reverse("blogs:blog_detail", args=[blog.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["blog"], blog)
