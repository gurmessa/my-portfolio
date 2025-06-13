
from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Project, ProjectKeyFeature


class ProjectKeyFeatureInline(admin.TabularInline):
    model = ProjectKeyFeature
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectKeyFeatureInline]
    list_display = ("name", "start_date", "end_date", "is_open_source")
    search_fields = ("name", "description")
    list_filter = ("tech_stacks", "start_date", "end_date")
    prepopulated_fields = {"slug": ("name",)}