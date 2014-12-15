"""The first team"""
class Team1(object):
	"""Initialization"""
    def __init__(self, scoreRec):
        self.scoreRec = []

    def addscore(score):
        self.scoreRec =+ score
        displayscore()

    def displayscore():
        print 'Team1: ' + self.scoreRec

"""The second team"""
class Team2(object):
    """Initialization"""
    def __init__(self, scoreRec):
        self.scoreRec = []

    def addscore(score):
        self.scoreRec =+ score
        displayscore()

    def displayscore():
        print 'Team1: ' + self.scoreRec

if __name__: '__main__':
    team1 = Team1()
    team2 = Team2()
    team = input('Which team to score? ( 1-team1, 2-team2 ):')

    if chosen == 1:
    	score = input('Input score of team1:')
    	team1.addscore(score)
    else:
        score = input('Input score of team2:')
        team2.addscore(score)