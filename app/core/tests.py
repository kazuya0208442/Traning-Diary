from django.test import TestCase
from .change_link import change_link
from .day_computed import day_computed
import datetime

# Create your tests here.
class TestCi(TestCase):

    def test_daycomputed(self):
        self.assertEqual(day_computed(datetime.date.today() + datetime.timedelta(days=1)), 1)

    def test_change_link(self):
        string = '<iframe width="560" height="315" src="https://www.youtube.com/embed/eZA0AnSdbBI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        ans = '<div class="wrapper"> <iframe width="560" height="315" src="https://www.youtube.com/embed/eZA0AnSdbBI?autoplay=1&mute=1&start=25" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> </div>'
        self.assertEqual(change_link(string, auto=1, start=25), ans)