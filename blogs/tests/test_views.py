from django.test import TestCase
from django.urls import reverse
from blogs.models import Blog
from blogs.tests.factories import BlogFactory, TagFactory, CategoryFactory


class BlogListViewTest(TestCase):

    def setUp(self):
        self.tag_one = TagFactory(name="Test Tag")
        self.tag_two = TagFactory(name="Another Tag")
        self.category_one = CategoryFactory(name="Test Category")
        self.category_two = CategoryFactory(name="Another Category")

        self.blog_category_one_and_tag_one = BlogFactory(
            category=self.category_one,
            tags=[
                self.tag_one,
            ],
        )
        self.blog_category_two = BlogFactory(
            category=self.category_two,
        )
        self.blog_tag_two = BlogFactory(
            tags=[
                self.tag_two,
            ]
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

    def test_filter_by_tag_slug(self):
        response = self.client.get(
            reverse("blogs:blog_list") + f"?tag={self.tag_two.name}"
        )
        self.assertEqual(response.status_code, 200)
        blogs = response.context["blogs"]
        self.assertEqual(len(blogs), 1)
        self.assertEqual(blogs[0].title, self.blog_tag_two.title)

    def test_filter_by_category_slug(self):
        response = self.client.get(
            reverse("blogs:blog_list"), {"category": self.category_two.name}
        )
        # response = self.client.get(reverse("blogs:blog_list")+f"?category={self.category_two.name}")
        self.assertEqual(response.status_code, 200)
        blogs = response.context["blogs"]
        self.assertEqual(len(blogs), 1)
        self.assertEqual(blogs[0].title, self.blog_category_two.title)

    def test_filter_no_match(self):
        response = self.client.get(reverse("blogs:blog_list"), {"tag": "unknown"})
        self.assertEqual(response.status_code, 200)
        blogs = response.context["blogs"]
        self.assertEqual(len(blogs), 0)

    def test_filter_by_tag_and_category(self):
        response = self.client.get(
            reverse("blogs:blog_list"),
            {"tag": self.tag_one.name, "category": self.category_one.name},
        )
        self.assertEqual(response.status_code, 200)
        blogs = response.context["blogs"]
        self.assertEqual(len(blogs), 1)
        self.assertEqual(blogs[0].title, self.blog_category_one_and_tag_one.title)


class BlogDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a blog post for detail view tests
        BlogFactory(
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
