# tests/factories.py

import factory
from factory.django import DjangoModelFactory
from blogs.models import Blog, Tag, Category
from django.utils.text import slugify


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Sequence(lambda n: f"Tag {n}")
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"Category {n}")
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))


class BlogFactory(DjangoModelFactory):
    class Meta:
        model = Blog

    title = factory.Sequence(lambda n: f"Blog {n}")
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    content = "Sample content"
    status = Blog.StatusChoices.PUBLISHED
    published_date = factory.Faker("date_time_this_year")
    category = factory.SubFactory(CategoryFactory)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            for tag in extracted:
                self.tags.add(tag)
