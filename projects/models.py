from django.db import models
from ckeditor.fields import RichTextField
from core.models import TechStack


class Project(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="project_images/", blank=True, null=True)
    tech_stacks = models.ManyToManyField(TechStack, related_name="projects", blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = RichTextField()
    demo_link = models.URLField(blank=True, null=True)
    source_code = models.URLField(blank=True, null=True)

    @property
    def is_open_source(self):
        return self.source_code is not None and self.source_code != ""

    def __str__(self):
        return self.name


class ProjectKeyFeature(models.Model):
    short_description = models.TextField()
    project = models.ForeignKey(
        Project, related_name="key_features", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.short_description
