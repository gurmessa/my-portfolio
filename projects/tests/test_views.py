from django.test import TestCase
from django.urls import reverse
from .factories import ProjectFactory


class ProjectListViewTest(TestCase):
    def setUp(self):
        self.projects = ProjectFactory.create_batch(2)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("projects:project_list"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("projects:project_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects/project_list.html")

    def test_view_passes_correct_context(self):
        response = self.client.get(reverse("projects:project_list"))
        self.assertEqual(response.status_code, 200)
        projects = response.context["projects"]
        self.assertEqual(list(projects), self.projects)


class ProjectDetailViewTest(TestCase):
    def setUp(self):
        self.project = ProjectFactory()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f"/projects/{self.project.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(
            reverse("projects:project_detail", args=[self.project.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(
            reverse("projects:project_detail", args=[self.project.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects/project_detail.html")

    def test_view_passes_correct_context(self):
        response = self.client.get(
            reverse("projects:project_detail", args=[self.project.pk])
        )
        self.assertEqual(response.status_code, 200)
        project = response.context["project"]
        self.assertEqual(project, self.project)
