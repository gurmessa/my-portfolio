import json
from django.shortcuts import render
from .models import PortfolioProfile, TechStackCategory, WorkExperience
from core.utils import get_experiences_data_json


def home(request):
    portfolio_profile = PortfolioProfile.get_solo()
    tech_stack_categories = TechStackCategory.objects.all().prefetch_related(
        "tech_stacks"
    )

    work_experiences = WorkExperience.objects.prefetch_related(
        "items", "tech_stacks"
    ).all()
    experiences_data_json = get_experiences_data_json(work_experiences)

    return render(
        request,
        "core/home.html",
        {
            "portfolio_profile": portfolio_profile,
            "tech_stack_categories": tech_stack_categories,
            "experiences_data_json": experiences_data_json,
        },
    )
