from core.models import PortfolioProfile


def global_object(request):
    portfolio_profile = PortfolioProfile.get_solo()
    return {"portfolio_profile": portfolio_profile}
