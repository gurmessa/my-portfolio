from django.test import TestCase
from core.models import TechStackCategory, TechStack, PortfolioProfile

class TechStackCategoryModelTest(TestCase):
    def test_create_tech_stack_category(self):
        category = TechStackCategory.objects.create(name='Web Development')
        self.assertEqual(str(category), 'Web Development')
        self.assertEqual(category.slug, 'web-development')

class TechStackModelTest(TestCase):
    def setUp(self):
        self.category = TechStackCategory.objects.create(name='Web Development', slug='web-development')

    def test_create_tech_stack(self):
        tech_stack = TechStack.objects.create(name='Django', category=self.category, image_url='http://example.com/django.png')
        self.assertEqual(str(tech_stack), 'Django')
        self.assertEqual(tech_stack.category, self.category)
        self.assertEqual(tech_stack.image_url, 'http://example.com/django.png')

class PortfolioProfileModelTest(TestCase):
    def test_create_portfolio_profile(self):
        profile = PortfolioProfile.objects.create(
            full_name='John Doe',
            job_title='Software Engineer',
            headline='Experienced Software Engineer',
            about_title='About Me',
            about_description='Detailed description about John Doe.',
            github_profile_link='http://github.com/johndoe',
            linkedin_profile_link='http://linkedin.com/in/johndoe',
            email='johndoe@example.com',
            phone='1234567890'
        )
        self.assertEqual(str(profile), 'John Doe')
        self.assertEqual(profile.full_name, 'John Doe')
        self.assertEqual(profile.job_title, 'Software Engineer')
        self.assertEqual(profile.headline, 'Experienced Software Engineer')
        self.assertEqual(profile.about_title, 'About Me')
        self.assertEqual(profile.about_description, 'Detailed description about John Doe.')
        self.assertEqual(profile.github_profile_link, 'http://github.com/johndoe')
        self.assertEqual(profile.linkedin_profile_link, 'http://linkedin.com/in/johndoe')
        self.assertEqual(profile.email, 'johndoe@example.com')
        self.assertEqual(profile.phone, '1234567890')

    def test_only_one_portfolio_profile_instance(self):
        PortfolioProfile.objects.create(
            full_name='John Doe',
            job_title='Software Engineer',
            headline='Experienced Software Engineer',
            about_title='About Me',
            about_description='Detailed description about John Doe.',
            github_profile_link='http://github.com/johndoe',
            linkedin_profile_link='http://linkedin.com/in/johndoe',
            email='johndoe@example.com',
            phone='1234567890'
        )
        with self.assertRaises(Exception):
            PortfolioProfile.objects.create(
                full_name='Jane Doe',
                job_title='Software Engineer',
                headline='Experienced Software Engineer',
                about_title='About Me',
                about_description='Detailed description about Jane Doe.',
                github_profile_link='http://github.com/janedoe',
                linkedin_profile_link='http://linkedin.com/in/janedoe',
                email='janedoe@example.com',
                phone='0987654321'
            )
