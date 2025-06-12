from django.contrib import admin
from .models import (
    TechStackCategory,
    TechStack,
    PortfolioProfile,
    WorkExperience,
    WorkExperienceItem,
)


class TechStackInline(admin.TabularInline):
    model = TechStack
    extra = 1  # Number of extra empty forms


class TechStackCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [TechStackInline]


class TechStackAdmin(admin.ModelAdmin):
    list_display = ("name", "category", )
    search_fields = ("name",)
    list_filter = ("category",)


class PortfolioProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("full_name", "job_title", "headline",)}),
        ("About Section", {"fields": ("about_title", "about_description")}),
        (
            "Contact Information",
            {
                "fields": (
                    "resume",
                    "github_profile_link",
                    "linkedin_profile_link",
                    "email",
                    "phone",
                )
            },
        ),
    )


class WorkExperienceItemInline(admin.TabularInline):
    model = WorkExperienceItem
    extra = 2


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ("company_name", "start_date", "end_date", "role", "location")
    search_fields = ("company_name", "role", "location")
    list_filter = ("start_date", "end_date")
    inlines = [WorkExperienceItemInline]


# Register your models here.
admin.site.register(TechStackCategory, TechStackCategoryAdmin)
admin.site.register(TechStack, TechStackAdmin)
admin.site.register(PortfolioProfile, PortfolioProfileAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
