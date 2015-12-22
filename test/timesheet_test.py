import unittest
from openpyxl import Workbook
import os
from ..src.timesheet import Timesheet
from ..src.workentry import Workentry

class TestTimesheet(unittest.TestCase):
    def test_read_timesheet(self):
        workbook = Workbook()
        workbook.active.title = "Zeiten"
        workbook.create_sheet("Summen")
        workbook.save("test.xlsx")
        timesheet = Timesheet("test.xlsx")
        workentry = Workentry("Coaching und so", "8", "17")
        timesheet.append_workentry(workentry)

        os.remove("test.xlsx")

    def test_timesheet_summary(self):
        timesheet = Timesheet("test/test_timesheet_summary.xlsx")
        self.assertEqual(timesheet.calculate_sum_working_time(), 26.5)

    def test_set_sum(self):
        timesheet = Timesheet("test/test_timesheet_summary.xlsx")
        timesheet.set_sum_working_time(5)

    def test_get_sum(self):
        timesheet = Timesheet("test/test_timesheet_summary.xlsx")
        self.assertEqual(timesheet.get_sum_working_time(), 26.5)

    def test_get_diff_normative_working_time(self):
        timesheet = Timesheet("test/test_timesheet_summary.xlsx")
        self.assertEqual(timesheet.get_diff_normative_actual_working_time_in_hours(), 69.5)

    def test_get_reamining_working_days(self):
        timesheet = Timesheet("test/test_timesheet_summary.xlsx")
        self.assertEqual(timesheet.get_remaining_days(), 8.6875)


if __name__ == '__main__':
    unittest.main()
