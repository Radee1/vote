import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Poll

class UrlTest(TestCase):

    def testPollsPage(self):
        response = self.client.get('/polls')
        print(response)

        self.assertEqual(response.status_code, 200)

