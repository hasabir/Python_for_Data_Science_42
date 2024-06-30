import datetime
import time

total_seconds = time.time()
formatted_seconds = "{:,.4f}".format(total_seconds)

print("Seconds since January 1, 1970:", formatted_seconds, "or", "{:.2e}".format(total_seconds), "in scientific notation")
print(datetime.date.today().strftime('%B %d %Y'))