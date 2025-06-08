# tests/factories.py
import factory
from factory.django import DjangoModelFactory
from django.utils.text import slugify
from core.models import TechStackCategory, TechStack 

class TechStackCategoryFactory(DjangoModelFactory):
    class Meta:
        model = TechStackCategory

    name = factory.Iterator(["Frontend", "Backend"])
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))


class TechStackFactory(DjangoModelFactory):
    class Meta:
        model = TechStack

    name = factory.Faker("word")
    category = factory.SubFactory(TechStackCategoryFactory)
    image_url = factory.Faker("image_url")
