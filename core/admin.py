from django.contrib import admin
from .models import TechStackCategory, TechStack, PortfolioProfile

# Custom admin class for TechStackCategory
class TechStackCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

# Custom admin class for TechStack
class TechStackAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image')
    search_fields = ('name',)
    list_filter = ('category',)
    readonly_fields = ('image',)

# Custom admin class for PortfolioProfile
class PortfolioProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('full_name', 'job_title', 'headline', 'short_bio')
        }),
        ('About Section', {
            'fields': ('about_title', 'about_description')
        }),
        ('Contact Information', {
            'fields': ('resume', 'github_profile_link', 'linkedin_profile_link', 'email', 'phone')
        }),
    )
    readonly_fields = ('resume',)

# Register your models here.
admin.site.register(TechStackCategory, TechStackCategoryAdmin)
admin.site.register(TechStack, TechStackAdmin)
admin.site.register(PortfolioProfile, PortfolioProfileAdmin)
