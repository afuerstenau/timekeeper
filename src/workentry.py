import time

class Workentry:
    def __init__(self, description, starttime, endtime):
            self._description = description
            self._starttime = self.string_to_time(starttime)

    def description(self):
        return self._description

    def starttime(self):
        return self._starttime

    def string_to_time(self, string):
        y,d,m,H,M,S,ZS,HS,TS = time.localtime()
        H = 8
        M = 0
        S = 0
        ZS = 0
        HS = 0
        TS = 0
        time_tupel = y,d,m,H,M,S,ZS,HS,TS
        alex_time = time.mktime(time_tupel)
        return alex_time
