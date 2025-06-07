from django.test import TestCase, Client
from django.urls import reverse
from core.models import PortfolioProfile, TechStackCategory, TechStack


class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.portfolio_profile = PortfolioProfile.objects.create(
            full_name="John Doe",
            job_title="Software Engineer",
            headline="Experienced Software Engineer",
            about_title="About Me",
            about_description="Detailed description about John Doe.",
            github_profile_link="http://github.com/johndoe",
            linkedin_profile_link="http://linkedin.com/in/johndoe",
            email="johndoe@example.com",
            phone="1234567890",
        )
        self.category = TechStackCategory.objects.create(
            name="Web Development", slug="web-development"
        )
        self.tech_stack = TechStack.objects.create(
            name="Django",
            category=self.category,
            image_url="http://example.com/django.png",
        )

    def test_home_view(self):
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/home.html")
        self.assertEqual(response.context["portfolio_profile"], self.portfolio_profile)
        self.assertIn(self.category, response.context["tech_stack_categories"])
        self.assertIn(
            self.tech_stack,
            response.context["tech_stack_categories"][0].tech_stacks.all(),
        )
