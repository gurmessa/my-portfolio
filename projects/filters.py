import django_filters
from projects.models import Project, TechStack


class ProjectFilter(django_filters.FilterSet):
    tech_stack = django_filters.CharFilter(
        field_name="tech_stacks__name",
        lookup_expr="iexact",
        label="Filter by Tech Stack Name",
    )

    class Meta:
        model = Project
        fields = ["tech_stack"]
