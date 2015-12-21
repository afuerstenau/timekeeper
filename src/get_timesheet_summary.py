from timesheet import Timesheet
from workentry import Workentry
import sys
import time

if __name__ == '__main__':

    timesheet = Timesheet('/Users/afuerstenau/Library/Mobile Documents/com~apple~CloudDocs/Arbeitszeit aktuell.xlsx')

    sys.stdout.write("Arbeitszeit:"+ str(timesheet.get_sum_working_time()) +" Differenz:" +str(timesheet.get_diff_normative_actual_working_time_in_hours()) + "verbleibende Tage:" +str(timesheet.get_remaining_days()))
    sys.stdout.flush()
    sys.exit(0)
