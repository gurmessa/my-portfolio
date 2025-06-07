from django.contrib import admin
from .models import TechStackCategory, TechStack, PortfolioProfile


class TechStackInline(admin.TabularInline):
    model = TechStack
    extra = 1  # Number of extra empty forms


class TechStackCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [TechStackInline]


class TechStackAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "image_url")
    search_fields = ("name",)
    list_filter = ("category",)


class PortfolioProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("full_name", "job_title", "headline", "short_bio")}),
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


# Register your models here.
admin.site.register(TechStackCategory, TechStackCategoryAdmin)
admin.site.register(TechStack, TechStackAdmin)
admin.site.register(PortfolioProfile, PortfolioProfileAdmin)
