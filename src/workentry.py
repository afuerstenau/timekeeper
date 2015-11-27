import time
import sys


class Workentry:
    def __init__(self, description, starttime, endtime, lunchbreak=0):
            self._description = description
            self._starttime = self.string_to_time(starttime)
            self._endtime = self.string_to_time(endtime)
            if lunchbreak=="30":
                self._lunchbreak = "01:30"
            elif lunchbreak=="1":
                self._lunchbreak = "01:00"
            elif lunchbreak == "1,5":
                self._lunchbreak = "01:30"


    def description(self):
        return self._description

    def starttime(self):
        return time.strftime("%H:%M",self._starttime)

    def endtime(self):
        return time.strftime("%H:%M",self._endtime)

    def lunchbreak(self):
        return self._lunchbreak

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

if __name__ == '__main__':
    workentry = Workentry(sys.argv[1], sys.argv[2], sys.argv[3])
    sys.stdout.write(workentry.description() + " " + workentry.starttime() + "-" + workentry.endtime())
    sys.stdout.flush()
    sys.exit(0)
