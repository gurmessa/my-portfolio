from django.shortcuts import render
from .models import PortfolioProfile, TechStackCategory

def home(request):
    portfolio_profile = PortfolioProfile.get_solo()
    tech_stack_categories = TechStackCategory.objects.all().prefetch_related('tech_stacks')
    return render(request, 'core/home.html', {
        'portfolio_profile': portfolio_profile,
        'tech_stack_categories': tech_stack_categories
    })
