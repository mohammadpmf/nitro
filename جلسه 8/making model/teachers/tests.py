from django.test import TestCase
from django.shortcuts import reverse

from .models import Teacher

class HarChiDeletMikhad(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(name='Ali',
        surname='Alavi',
        nat_code='123',
        age=30,
        description='A short Description',
        decimal_age=1.2,
        date_time='2020-11-11 10:43',
    )

    def test_finding_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_finding_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_finding_teacher_name_in_page(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, self.teacher.name)

