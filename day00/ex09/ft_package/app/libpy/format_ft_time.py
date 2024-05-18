import time
import datetime

seconds = time.time()

dt1 = datetime.datetime(year=1970, month=1, day=1)
dt2 = datetime.datetime.utcfromtimestamp(seconds)

dt = dt2 - dt1

total_seconds = dt.total_seconds()
print("Seconds since January 1, 1970:", total_seconds, "or", "{:.2e}".format(total_seconds), "in scientific notation")
print(datetime.date.today().strftime('%B %d %Y'))