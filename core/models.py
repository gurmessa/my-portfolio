from django.db import models
from django.utils.text import slugify
from solo.models import SingletonModel

# TechStackCategory model
class TechStackCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

# TechStack model
class TechStack(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(TechStackCategory, on_delete=models.CASCADE, related_name='tech_stacks')
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# PortfolioProfile model
class PortfolioProfile(SingletonModel):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    headline = models.TextField(blank=True, null=True)
    about_title = models.CharField(max_length=255, blank=True, null=True)
    about_description = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    github_profile_link = models.URLField(blank=True, null=True)
    linkedin_profile_link = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.full_name if self.full_name else 'Portfolio Profile'

    class Meta:
        verbose_name = 'Portfolio Profile'
        verbose_name_plural = 'Portfolio Profile'
