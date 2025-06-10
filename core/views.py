import json
from django.shortcuts import render
from .models import PortfolioProfile, TechStackCategory, WorkExperience
from core.utils import get_experiences_data_json
from projects.models import Project


def home(request): 
    tech_stack_categories = TechStackCategory.objects.all().prefetch_related(
        "tech_stacks"
    )

    work_experiences = WorkExperience.objects.prefetch_related(
        "items", "tech_stacks"
    ).all()
    experiences_data_json = get_experiences_data_json(work_experiences)
    featured_projects = Project.featured_projects.all()

    return render(
        request,
        "core/home.html",
        {
            "tech_stack_categories": tech_stack_categories,
            "experiences_data_json": experiences_data_json,
            "projects": featured_projects,
        },
    )
