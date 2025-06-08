from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from projects.models import Project, ProjectKeyFeature
from core.tests.factories import TechStackFactory


class ProjectModelTest(TestCase):
    def setUp(self):
        self.tech_stack = TechStackFactory(name="python")
        self.project = Project.objects.create(
            name="Test Project",
            description="This is a test project.",
        )
        self.project.tech_stacks.add(self.tech_stack)
        self.project_key_feature = ProjectKeyFeature.objects.create(
            short_description="Test feature", project=self.project
        )

    def test_project_creation(self):
        self.assertEqual(self.project.name, "Test Project")
        self.assertEqual(self.project.description, "This is a test project.")
        self.assertIn(self.tech_stack, self.project.tech_stacks.all())
        self.assertIsNone(self.project.start_date)
        self.assertIsNone(self.project.end_date)
        self.assertIsNone(self.project.demo_link)
        self.assertIsNone(self.project.source_code)

    def test_project_is_open_source(self):
        self.project.source_code = "https://github.com/test/test-project"
        self.project.save()
        self.assertTrue(self.project.is_open_source)

        self.project.source_code = ""
        self.project.save()
        self.assertFalse(self.project.is_open_source)

    def test_project_str(self):
        self.assertEqual(str(self.project), "Test Project")


class ProjectKeyFeatureModelTest(TestCase):
    def setUp(self):
        self.tech_stack = TechStackFactory(name="python")
        self.project = Project.objects.create(
            name="Test Project",
            description="This is a test project.",
        )
        self.project.tech_stacks.add(self.tech_stack)
        self.project_key_feature = ProjectKeyFeature.objects.create(
            short_description="Test feature", project=self.project
        )

    def test_project_key_feature_creation(self):
        self.assertEqual(self.project_key_feature.short_description, "Test feature")
        self.assertEqual(self.project_key_feature.project, self.project)

    def test_project_key_feature_str(self):
        self.assertEqual(str(self.project_key_feature), "Test feature")

    def test_project_key_feature_relationship(self):
        self.assertEqual(self.project_key_feature.project, self.project)
        self.assertIn(self.project_key_feature, self.project.key_features.all())
