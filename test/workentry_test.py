import unittest
import time
from ..src.workentry import Workentry

class TestStringMethods(unittest.TestCase):

  def test_create_workentry_with_date(self):
      workentry = Workentry("listen to podcast", "8", "17:30")
      self.assertEqual(workentry.description(), "listen to podcast")
      self.assertEqual(workentry.starttime(), "08:00")
      self.assertEqual(workentry.endtime(), "17:30")

  def test_create_workentry_with_date(self):
      workentry = Workentry("listen to podcast", "09:30", "18", "1,5")
      self.assertEqual(workentry.description(), "listen to podcast")
      self.assertEqual(workentry.starttime(), "09:30")
      self.assertEqual(workentry.endtime(), "18:00")
      self.assertEqual(workentry.lunchbreak(), "01:30")

if __name__ == '__main__':
    unittest.main()
