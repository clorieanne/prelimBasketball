import unittest
from basketball.basketball import *

class TestBasketball(unittest.TestCase):
    def test_scoreRec(self):
        team = Team()
        self.assertEqual(team.scoreRec, 0)

    def test_addscore(self):
        team = Team()
        team.addscore(3)
        self.assertEqual(team.scoreRec, 3)

    def test_display(self):
    	team = Team()
        self.assertEqual(team.display(), 0)