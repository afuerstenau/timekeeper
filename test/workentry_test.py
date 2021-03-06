import unittest
import time
from ..src.workentry import Workentry

class TestStringMethods(unittest.TestCase):

  def test_create_workentry_with_date(self):
      workentry = Workentry("listen to podcast", "8", "17:30")
      self.assertEqual(workentry.description(), "listen to podcast")
      self.assertEqual(workentry.starttime(), "08:00")
      self.assertEqual(workentry.endtime(), "17:30")
      self.assertEqual(workentry.lunchbreak(), "00:00")
      self.assertEqual(workentry.working_time(), 9.5)

  def test_create_workentry_with_30_min_breaks(self):
      workentry = Workentry("listen to podcast", "8", "17:30", "0,5")
      self.assertEqual(workentry.lunchbreak(), "00:30")
      workentry = Workentry("listen to podcast", "8", "17:30", "0.5")
      self.assertEqual(workentry.lunchbreak(), "00:30")
      workentry = Workentry("listen to podcast", "8", "17:30", ".5")
      self.assertEqual(workentry.lunchbreak(), "00:30")
      workentry = Workentry("listen to podcast", "8", "17:30", ",5")
      self.assertEqual(workentry.lunchbreak(), "00:30")
      workentry = Workentry("listen to podcast", "8", "17:30", "30")
      self.assertEqual(workentry.lunchbreak(), "00:30")

  def test_create_workentry_with_45_min_breaks(self):
      workentry = Workentry("listen to podcast", "8", "17:30", "0,75")
      self.assertEqual(workentry.lunchbreak(), "00:45")
      workentry = Workentry("listen to podcast", "8", "17:30", "0.75")
      self.assertEqual(workentry.lunchbreak(), "00:45")
      workentry = Workentry("listen to podcast", "8", "17:30", ".75")
      self.assertEqual(workentry.lunchbreak(), "00:45")
      workentry = Workentry("listen to podcast", "8", "17:30", ",75")
      self.assertEqual(workentry.lunchbreak(), "00:45")
      workentry = Workentry("listen to podcast", "8", "17:30", "45")
      self.assertEqual(workentry.lunchbreak(), "00:45")


  def test_create_workentry_with_complex_date(self):
      workentry = Workentry("listen to podcast", "09:30", "18", "1.5")
      self.assertEqual(workentry.description(), "listen to podcast")
      self.assertEqual(workentry.starttime(), "09:30")
      self.assertEqual(workentry.endtime(), "18:00")
      self.assertEqual(workentry.lunchbreak(), "01:30")
      self.assertEqual(workentry.working_time(), 7)

if __name__ == '__main__':
    unittest.main()
