from django.test import TestCase
from django.urls import reverse


class TestIndexView(TestCase):
    """ Testing main view """

    def test_get(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/main.html')


class TestLibraryView(TestCase):
    """ Testing resources view """
    pass


class TestPostsView(TestCase):
    """ Testing posts view """

    def test_get(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/blog.html')


class TestStoriesView(TestCase):
    """ Testing stories view """

    def test_get(self):
        response = self.client.get(reverse('stories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/stories/stories.html')


    def test_post(self):
        data = {
            'name': 'John Doe',
            'case': 'Test case',
            'abuse_from_CPS_DCFS': 'Substantiated',
            'parental_alienation': 'Mild',
            'allegations': 'Yes',
            'falsified': 'No',
            'duration': 'Test duration',
            'money': 'Test money',
            'left_broken': 'Test left broken',
            'abuse_criteria': 'Test abuse criteria',
            'result': 'Test result'
        }
        response = self.client.post(reverse('stories'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/stories/stories_add.html')

class TestTestView(TestCase):
    """ Testing process_alienation_test view """
    def test_get(self):
        response = self.client.get(reverse('process_alienation_test'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/test-blocks/test.html')

    # TODO: write test with post request
    def test_post(self):
        pass