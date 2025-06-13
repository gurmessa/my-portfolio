from django.utils.text import slugify
from django.db import models
from ckeditor.fields import RichTextField
from core.models import TechStack


class FeaturedProjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(featured=True)


class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, blank=True)
    image = models.ImageField(upload_to="project_images/", blank=True, null=True)
    tech_stacks = models.ManyToManyField(TechStack, related_name="projects", blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = RichTextField()
    demo_link = models.URLField(blank=True, null=True)
    source_code = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)

    objects = models.Manager()  # Default manager
    featured_projects = FeaturedProjectManager()  # Custom manager for featured projects

    @property
    def is_open_source(self):
        return self.source_code is not None and self.source_code != ""

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProjectKeyFeature(models.Model):
    short_description = models.CharField(max_length=255)
    project = models.ForeignKey(
        Project, related_name="key_features", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.short_description
