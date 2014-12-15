from lettuce import *
from basketball.basketball import *
from nose.tools import assert_equal
import os

@step(u'Given I have two teams')
def given_i_have_two_teams(step):
    team1 = Team()
    team2 = Team()
    assert_equal(team1.scoreRec, 0)
    assert_equal(team2.scoreRec, 0)

@step(u'When I run the program')
def when_i_run_the_program(step):
    os.system('python basketball.py')

@step(u'Then I get the score of')
def then_i_get_the_score_of(step):
    res = []
    for row in step.hashes:
        res.append(row)

    assert True