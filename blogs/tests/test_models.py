from django.test import TestCase
from django.utils import timezone
from blogs.models import Category, Tag, Blog


class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(
            name="Technology", description="Tech related blogs"
        )
        self.assertEqual(category.slug, "technology")
        self.assertEqual(str(category), "Technology")

    def test_slug_generation(self):
        category = Category(name="Web Development")
        category.save()
        self.assertEqual(category.slug, "web-development")


class TagModelTest(TestCase):
    def test_create_tag(self):
        tag = Tag.objects.create(name="django")
        self.assertEqual(tag.slug, "django")
        self.assertEqual(str(tag), "django")

    def test_multiple_tags(self):
        tag1 = Tag.objects.create(name="Python")
        tag2 = Tag.objects.create(name="JavaScript")
        self.assertEqual(tag1.slug, "python")
        self.assertEqual(tag2.slug, "javascript")


class BlogModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Programming")
        self.tag1 = Tag.objects.create(name="Python")
        self.tag2 = Tag.objects.create(name="Django")

        self.blog = Blog.objects.create(
            title="Getting Started with Django",
            content="Learn Django basics",
            category=self.category,
        )
        self.blog.tags.add(self.tag1, self.tag2)

    def test_blog_creation(self):
        self.assertEqual(self.blog.status, Blog.StatusChoices.DRAFT)
        self.assertEqual(self.blog.view_count, 0)
        self.assertEqual(self.blog.tags.count(), 2)

    def test_slug_generation(self):
        self.assertEqual(self.blog.slug, "getting-started-with-django")

    def test_publish_method(self):
        self.blog.publish()
        self.assertEqual(self.blog.status, Blog.StatusChoices.PUBLISHED)
        self.assertIsNotNone(self.blog.published_date)

    def test_increment_views(self):
        self.blog.increment_views()
        self.assertEqual(self.blog.view_count, 1)
        self.blog.increment_views()
        self.assertEqual(self.blog.view_count, 2)

    def test_published_manager(self):
        self.assertEqual(Blog.published.count(), 0)
        # Create a published blog

        published_blog = Blog.objects.create(
            title="Published Blog",
            content="This is published",
            status=Blog.StatusChoices.PUBLISHED,
        )

        # Should only return published blogs
        published_blogs = Blog.published.all()
        self.assertEqual(published_blogs.count(), 1)
        self.assertEqual(published_blogs[0].title, "Published Blog")

    def test_default_manager(self):
        Blog.objects.create(
            title="Published Blog",
            content="This is published",
            status=Blog.StatusChoices.PUBLISHED,
        )
        # Default manager should return all blogs
        all_blogs = Blog.objects.all()
        self.assertEqual(all_blogs.count(), 2)
