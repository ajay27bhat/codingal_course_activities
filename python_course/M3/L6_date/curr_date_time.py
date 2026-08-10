import calendar
import datetime
import time

# Current date and time
current_time = time.strftime("%H:%M:%S")
current_date = datetime.date.today()

print("Current Date:", current_date)
print("Current Time:", current_time)

# Display calendar of the current month
year = current_date.year
month = current_date.month

print("\nCalendar:")
print(calendar.month(year, month))