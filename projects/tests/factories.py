from django.core.files.uploadedfile import SimpleUploadedFile
import factory
from factory.django import DjangoModelFactory
from core.tests.factories import TechStackFactory
from projects.models import Project, ProjectKeyFeature


class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project

    name = factory.Faker("sentence", nb_words=3)
    image = factory.LazyAttribute(
        lambda _: SimpleUploadedFile(
            name="test.jpg", content=b"fake-image-content", content_type="image/jpeg"
        )
    )
    start_date = factory.Faker("date_this_decade")
    end_date = factory.Faker("date_this_decade")
    description = factory.Faker("paragraph")
    demo_link = factory.Faker("url")
    source_code = factory.Faker("url")

    @factory.post_generation
    def tech_stacks(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for stack in extracted:
                self.tech_stacks.add(stack)
        else:
            self.tech_stacks.add(*TechStackFactory.create_batch(1))

    @factory.post_generation
    def key_features(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for feature in extracted:
                feature.project = self
                feature.save()
        else:
            ProjectKeyFeatureFactory.create_batch(2, project=self)


class ProjectKeyFeatureFactory(DjangoModelFactory):
    class Meta:
        model = ProjectKeyFeature

    short_description = factory.Faker("sentence")
    project = factory.SubFactory(ProjectFactory)
