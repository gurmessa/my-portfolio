from django.contrib import admin
from .models import TechStackCategory, TechStack, PortfolioProfile

class TechStackInline(admin.TabularInline):  # Or use StackedInline
    model = TechStack
    extra = 1  # Number of extra empty forms


# Custom admin class for TechStackCategory
class TechStackCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [TechStackInline]  # Inline TechStack model in the category admin

# Custom admin class for TechStack
class TechStackAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image_url')
    search_fields = ('name',)
    list_filter = ('category',)



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
    
# Register your models here.
admin.site.register(TechStackCategory, TechStackCategoryAdmin)
admin.site.register(TechStack, TechStackAdmin)
admin.site.register(PortfolioProfile, PortfolioProfileAdmin)
