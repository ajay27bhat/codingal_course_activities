# Program to demonstrate DateTime Operations

from datetime import datetime, timedelta

# 1. Get current date and time
now = datetime.now()
print("Current Date and Time:", now)

# 2. Get individual date and time values
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# 3. Format date and time
print("Formatted Date:", now.strftime("%d-%m-%Y"))
print("Formatted Time:", now.strftime("%H:%M:%S"))

# 4. Create a specific date
birthday = datetime(2010, 5, 15)
print("Birthday:", birthday.strftime("%d-%m-%Y"))

# 5. Add days
future_date = now + timedelta(days=7)
print("Date after 7 days:", future_date.strftime("%d-%m-%Y"))

# 6. Subtract days
past_date = now - timedelta(days=7)
print("Date 7 days ago:", past_date.strftime("%d-%m-%Y"))

# 7. Find difference between two dates
date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 1, 10)

difference = date2 - date1
print("Difference between dates:", difference.days, "days")