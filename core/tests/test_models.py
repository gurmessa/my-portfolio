from django.test import TestCase
from core.models import (
    TechStackCategory,
    TechStack,
    PortfolioProfile,
    WorkExperience,
    WorkExperienceItem,
)


class TechStackCategoryModelTest(TestCase):
    def test_create_tech_stack_category(self):
        category = TechStackCategory.objects.create(name="Web Development")
        self.assertEqual(str(category), "Web Development")
        self.assertEqual(category.slug, "web-development")


class TechStackModelTest(TestCase):
    def setUp(self):
        self.category = TechStackCategory.objects.create(
            name="Web Development", slug="web-development"
        )

    def test_create_tech_stack(self):
        tech_stack = TechStack.objects.create(
            name="Django",
            category=self.category,
            image_url="http://example.com/django.png",
        )
        self.assertEqual(str(tech_stack), "Django")
        self.assertEqual(tech_stack.category, self.category)
        self.assertEqual(tech_stack.image_url, "http://example.com/django.png")


class PortfolioProfileModelTest(TestCase):
    def test_create_portfolio_profile(self):
        profile = PortfolioProfile.objects.create(
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
        self.assertEqual(str(profile), "John Doe")
        self.assertEqual(profile.full_name, "John Doe")
        self.assertEqual(profile.job_title, "Software Engineer")
        self.assertEqual(profile.headline, "Experienced Software Engineer")
        self.assertEqual(profile.about_title, "About Me")
        self.assertEqual(
            profile.about_description, "Detailed description about John Doe."
        )
        self.assertEqual(profile.github_profile_link, "http://github.com/johndoe")
        self.assertEqual(
            profile.linkedin_profile_link, "http://linkedin.com/in/johndoe"
        )
        self.assertEqual(profile.email, "johndoe@example.com")
        self.assertEqual(profile.phone, "1234567890")

    def test_only_one_portfolio_profile_instance(self):
        PortfolioProfile.objects.create(
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
        with self.assertRaises(Exception):
            PortfolioProfile.objects.create(
                full_name="Jane Doe",
                job_title="Software Engineer",
                headline="Experienced Software Engineer",
                about_title="About Me",
                about_description="Detailed description about Jane Doe.",
                github_profile_link="http://github.com/janedoe",
                linkedin_profile_link="http://linkedin.com/in/janedoe",
                email="janedoe@example.com",
                phone="0987654321",
            )


class WorkExperienceModelTest(TestCase):
    def setUp(self):
        self.category = TechStackCategory.objects.create(name="Web Development")
        self.tech_stack = TechStack.objects.create(
            name="Python", category=self.category
        )
        self.work_experience = WorkExperience.objects.create(
            start_date="2023-01-01",
            end_date="2023-12-31",
            company_name="Tech Corp",
            role="Software Engineer",
            location="San Francisco",
        )
        self.work_experience.tech_stacks.add(self.tech_stack)

    def test_create_work_experience(self):
        self.assertEqual(self.work_experience.company_name, "Tech Corp")

    def test_work_experience_without_end_date(self):
        self.work_experience.end_date = None
        self.work_experience.save()

    def test_work_experience_with_tech_stacks(self):
        self.assertIn(self.tech_stack, self.work_experience.tech_stacks.all())


class WorkExperienceItemModelTest(TestCase):
    def setUp(self):
        self.work_experience = WorkExperience.objects.create(
            start_date="2023-01-01",
            end_date="2023-12-31",
            company_name="Tech Corp",
            role="Software Engineer",
            location="San Francisco",
        )

    def test_create_work_experience_item(self):
        item = WorkExperienceItem.objects.create(
            description="Responsible for developing new features.",
            work_experience=self.work_experience,
        )

        self.assertEqual(str(item), "Responsible for developing new features.")
        self.assertEqual(item.description, "Responsible for developing new features.")

    def test_work_experience_item_relationship(self):

        item = WorkExperienceItem.objects.create(
            description="Responsible for developing new features.",
            work_experience=self.work_experience,
        )

        self.assertEqual(item.work_experience, self.work_experience)
        self.assertIn(item, self.work_experience.items.all())
