import array
from . import Ranking

class Snippet:
    """simple class for Snippet"""
    def __init__(self, textFile: str, videoFile: str):
        self.textFile = textFile
        self.videoFile = videoFile

def initialise():
    trackingArray = []
    for i in range(11):
        defaultContents = "default" + str(i)
        trackingArray.append(Snippet(defaultContents, defaultContents))
    Ranking.initialise()
    return trackingArray


