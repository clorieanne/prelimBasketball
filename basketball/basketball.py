"""The Team"""
result = []
class Team(object):
    """Initialization"""
    def __init__(self):
        self.scoreRec = 0

    def addscore(self, score):
        self.scoreRec = self.scoreRec + int(score)

    def display(self):
    	return self.scoreRec

if __name__=='__main__':
    team1 = Team()
    team2 = Team()

    i = 1
    while i == 1:
        team = input('Which team to score? ( 1-team1, 2-team2 ):')

        if team == 1:
    	    score = input('Input score of team1:')
    	    team1.addscore(score)
        elif team == 2:
            score = input('Input score of team2:')
            team2.addscore(score)
        else:
        	print 'error: no such team'

        a = 'Team1: ' + str(team1.display())
        b =  'Team2: ' + str(team2.display())
        print a
        print b

        result.append(a)
        result.append(b)

        i = input('GameOver? (0-yes 1-no): ')
