from django.db import models
from django.utils.text import slugify
from solo.models import SingletonModel


class TechStackCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Tech Stack Category"
        verbose_name_plural = "Tech Stack Categories"


class TechStack(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        TechStackCategory, on_delete=models.CASCADE, related_name="tech_stacks"
    )
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class PortfolioProfile(SingletonModel):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    headline = models.TextField(blank=True, null=True)
    about_title = models.CharField(max_length=150, blank=True, null=True)
    about_description = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    github_profile_link = models.URLField(blank=True, null=True)
    linkedin_profile_link = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.full_name if self.full_name else "Portfolio Profile"

    class Meta:
        verbose_name = "Portfolio Profile"
        verbose_name_plural = "Portfolio Profile"


class WorkExperience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    company_name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    tech_stacks = models.ManyToManyField(TechStack, blank=True)

    def __str__(self):
        return f"{self.role} at {self.company_name}"


class WorkExperienceItem(models.Model):
    description = models.CharField(max_length=255)
    work_experience = models.ForeignKey(
        WorkExperience, on_delete=models.CASCADE, related_name="items"
    )

    def __str__(self):
        return self.description
