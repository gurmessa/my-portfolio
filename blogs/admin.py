from django.contrib import admin
from .models import Category, Tag, Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "description")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "published_date", "category", "view_count")
    list_filter = ("status", "category", "tags")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content")
    date_hierarchy = "published_date"
    filter_horizontal = ("tags",)

    fieldsets = (
        (None, {"fields": ("title", "slug", "content", "category", "tags")}),
    )

    actions = ["publish_blogs"]

    def publish_blogs(self, request, queryset):
        for blog in queryset:
            blog.publish()
        self.message_user(request, "Selected blogs have been published.")

    publish_blogs.short_description = "Publish selected blogs"
