from django.test import TestCase
from .models import Poll
#from .models import Poll, Choice, Vote
from django.urls import reverse


class ModelTest(TestCase):

    def testPollModel(self):
        poll = Poll.objects.create(owner="Dada1",text="Test Text" )
        self.assertEquals(str(poll), 'Test_Poll')
        print("IsInstance : ",isinstance(poll,Poll))
        self.assertTrue(isinstance(poll,Poll))


class IndexTest(TestCase):

    def testIndexPage(self):
        response = self.client.get('/')
        print(response)
        self.assertEqual(response.status_code, 200)


class LoginTest(TestCase):

    def testLoginPage(self):
        response = self.client.get('accounts:login')
        print(response)


class SignupTest(TestCase):

    def testSignUpPage(self):
        response = self.client.get('accounts:register')
        print(response)


class NotFoundTest(TestCase):

    def test404Page(self):
        response = self.client.get('accounts:registerhk')
        print(response)
        self.assertEqual(response.status_code, 200)


'''
class ModelTestCase(TestCase):
    def setUp(self):
        Diagnosis.objects.create(patient_name="John Doe", test_name="Malaria Test", diagnosis="Malaria Positive")
        Diagnosis.objects.create(patient_name="Jane Din", test_name="Sputum test", diagnosis="Covid Positive")
'''