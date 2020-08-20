from django.test import TestCase
from .models import Project
from datetime import datetime
from django.contrib.auth.models import User

# Create your tests here.
class TestProject(TestCase):
    def setUp(self):
        ''' method called before each test case'''
        self.test_user = User(username='Linda', password='123')
        self.test_user.save()

        self.test_project = Project(image='images/test.jpg', title='some text',description='some info', user=self.test_user, link='https://www.google.com', date_posted=datetime.now())

    def test_instance(self):
        self.assertTrue(isinstance(self.test_project, Project))

    def test_save_and_delete(self):
        self.test_project.save_project()
        self.assertEqual(len(Project.objects.all()), 1)
        self.test_project.delete_project()
        self.assertEqual(len(Project.objects.all()), 0)

    def test_search_project(self):
        self.test_project.save_project()
        res = Project.search_by_title('some text')
        self.assertIsNotNone(res)

    def tearDown(self):
        self.test_user.delete() 
        project.objects.all().delete()

class ProfileTest(TestCase):
    ''' test class for Profile model'''
    def setUp(self):
        ''' method called before each test case'''
        self.user = User.objects.create_user(username='Water')

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.user.delete()

    def test_profile_creation(self):
        ''' method to test profile instance is created only once for each user '''
        self.assertIsInstance(self.user.profile, Profile)
        self.user.save()
        self.assertIsInstance(self.user.profile, Profile)
                