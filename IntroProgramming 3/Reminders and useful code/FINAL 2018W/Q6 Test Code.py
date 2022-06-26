from typing import List
class Score(object):
    def __init__(self, name: str, score: int):
        self.name = name # Public, read-only
        self.score = score  # Public, read-only

    def __repr__(self):
        return 'Score("{}",{})'.format(self.name, self.score)

def normalize(projects: List[Score]) -> List[Score]:
    #I FINISH
    highscore = projects[0].score
    for totalscore in range (len(projects)-1):
        if projects[totalscore+1].score > highscore:
            highscore = projects[totalscore+1].score
    scoremult = 100/highscore
    for scorei in projects:
        scorei.score = int(scorei.score * scoremult)

    return projects


scores = [Score("Leslie", 40), Score("Bobby", 23), Score("Adrian", 42)]
print(normalize(scores))# Expected output: [Score("Leslie",95), Score("Bobby",54), Score("Adrian",100)]