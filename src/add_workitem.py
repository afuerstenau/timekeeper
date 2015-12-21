from timesheet import Timesheet
from workentry import Workentry
import sys
import time

if __name__ == '__main__':
    lunchbreak = ""
    try:
        lunchbreak = sys.argv[4]
    except Exception as e:
        pass
    workentry = Workentry(sys.argv[1], sys.argv[2], sys.argv[3], lunchbreak)
    timesheet = Timesheet('/Users/afuerstenau/Library/Mobile Documents/com~apple~CloudDocs/Arbeitszeit aktuell.xlsx')
    sum_working_time = timesheet.append_workentry(workentry)
    sys.stdout.write(workentry.description() + " " + workentry.starttime() + "-" + workentry.endtime()+ "\nSumme:" + str(sum_working_time))
    sys.stdout.flush()
    sys.exit(0)
