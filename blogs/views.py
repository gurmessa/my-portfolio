from django.views.generic import ListView, DetailView
from blogs.models import Blog
from blogs.filters import BlogFilter


class BlogListView(ListView):
    model = Blog
    template_name = "blogs/blog_list.html"
    context_object_name = "blogs"
    filterset_class = BlogFilter

    """
    def get_queryset(self):
        return Blog.published.order_by("-published_date")
    """

    def get_queryset(self):
        queryset = Blog.published.order_by("-published_date")
        self.filterset = BlogFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = self.request.GET.get("category")
        tag = self.request.GET.get("tag")

        if category:
            list_type = category
        elif tag:
            list_type = tag
        else:
            list_type = "Latest"

        context["list_type"] = list_type
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogs/blog_detail.html"
    context_object_name = "blog"

    def get_queryset(self):
        return Blog.published.all()
