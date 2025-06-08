from django.views.generic import ListView, DetailView
from .models import Project
from projects.filters import ProjectFilter


class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related("tech_stacks")
        self.filterset = ProjectFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Pass width to template (with default value 0)
        tech_stack = self.request.GET.get("tech_stack", "All")

        context["tech_stack"] = tech_stack
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"
