from django.test import TestCase
from .models import Poll

class ModelTest(TestCase):

    def testPollModel(self):
        poll = Poll.objects.create(owner="Dada1",text="Test Text" )
        self.assertEquals(str(poll), 'Test_Poll')
        print("IsInstance : ",isinstance(poll,Poll))
        self.assertTrue(isinstance(poll,Poll))