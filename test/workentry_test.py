import unittest
import time
from ..src.workentry import Workentry

class TestStringMethods(unittest.TestCase):

  def test_create_workentry_with_date(self):
      workentry = Workentry("listen to podcast", "8", "17:30")
      self.assertEqual(workentry.description(), "listen to podcast")
      y,d,m,H,M,S,ZS,HS,TS = time.localtime()

      H = 8
      M = 0
      S = 0
      ZS = 0
      HS = 0
      TS = 0
      starttime_tupel = y,d,m,H,M,S,ZS,HS,TS
      starttime = time.mktime(starttime_tupel)
      endtime = time.strptime("17:30", "%H:%M")
      self.assertEqual(workentry.starttime(), starttime)


if __name__ == '__main__':
    unittest.main()
