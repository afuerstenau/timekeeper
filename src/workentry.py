import time

class Workentry:
    lunchbreak_30min_options = ["30", "0,5", "0.5", ".5", ",5"]
    lunchbreak_one_and_half_hours_options = ["1,5", "1.5"]
    def __init__(self, description, starttime, endtime, lunchbreak=0):
            self._description = description
            self._starttime = self.string_to_time(starttime)
            self._endtime = self.string_to_time(endtime)
            self._lunchbreak = "00:00"
            self._lunchbreak_as_number = 0
            if lunchbreak in self.lunchbreak_30min_options:
                self._lunchbreak = "00:30"
                self._lunchbreak_as_number = 0.5
            elif lunchbreak=="1":
                self._lunchbreak = "01:00"
                self._lunchbreak_as_number = 1
            elif lunchbreak in self.lunchbreak_one_and_half_hours_options:
                self._lunchbreak = "01:30"
                self._lunchbreak_as_number = 1.5


    def description(self):
        return self._description

    def starttime(self):
        return time.strftime("%H:%M",self._starttime)

    def endtime(self):
        return time.strftime("%H:%M",self._endtime)

    def lunchbreak(self):
        return self._lunchbreak

    def working_time(self):
        return (time.mktime(self._endtime)-time.mktime(self._starttime))/3600-self._lunchbreak_as_number

    def string_to_time(self, string):
        y,d,m,H,M,S,ZS,HS,TS = time.localtime()
        if ":" in string:
            position=string.find(":")
            H = int(string[:position])
            M = int(string[position+1:])
        else:
            H = int(string)
            M = 0
        S = 0
        ZS = 0
        HS = 0
        TS = 0
        time_tupel = y,d,m,H,M,S,ZS,HS,TS
        return time_tupel
