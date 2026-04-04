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

    def test_only_featured_projects_displayed(self):
        # Assuming you have a Project model and a way to create projects
        from projects.tests.factories import ProjectFactory
        featured_project = ProjectFactory( name="Project 1", featured=True)
        ProjectFactory(name="Project 2", featured=False)
        
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("projects", response.context)
        self.assertEqual(len(response.context["projects"]), 1)
        self.assertIn(featured_project, response.context["projects"])


class TermsOfServiceViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_terms_of_service_view_status_code(self):
        response = self.client.get(reverse("core:terms_of_service"))
        self.assertEqual(response.status_code, 200)

    def test_terms_of_service_view_uses_correct_template(self):
        response = self.client.get(reverse("core:terms_of_service"))
        self.assertTemplateUsed(response, "core/terms_of_service.html")

    def test_terms_of_service_displays_content(self):
        PortfolioProfile.objects.create(
            full_name="John Doe",
            terms_of_service="These are the terms of service.",
        )
        response = self.client.get(reverse("core:terms_of_service"))
        self.assertContains(response, "These are the terms of service.")

    def test_terms_of_service_displays_placeholder_when_empty(self):
        response = self.client.get(reverse("core:terms_of_service"))
        self.assertContains(response, "Terms of service have not been set yet.")


class PrivacyPolicyViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_privacy_policy_view_status_code(self):
        response = self.client.get(reverse("core:privacy_policy"))
        self.assertEqual(response.status_code, 200)

    def test_privacy_policy_view_uses_correct_template(self):
        response = self.client.get(reverse("core:privacy_policy"))
        self.assertTemplateUsed(response, "core/privacy_policy.html")

    def test_privacy_policy_displays_content(self):
        PortfolioProfile.objects.create(
            full_name="John Doe",
            privacy_policy="This is the privacy policy.",
        )
        response = self.client.get(reverse("core:privacy_policy"))
        self.assertContains(response, "This is the privacy policy.")

    def test_privacy_policy_displays_placeholder_when_empty(self):
        response = self.client.get(reverse("core:privacy_policy"))
        self.assertContains(response, "Privacy policy has not been set yet.")
