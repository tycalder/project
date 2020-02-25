class Ranking:
    """description of class"""
    current: int
    recent: int
    oldest: int

def update():
    Ranking.recent = Ranking.current
    Ranking.current = Ranking.oldest
    if Ranking.oldest == 9:
        Ranking.oldest = 0
    else:
        Ranking.oldest = Ranking.oldest + 1

def initialise():
    Ranking.current = 9
    Ranking.oldest = 0
    Ranking.recent = 8





