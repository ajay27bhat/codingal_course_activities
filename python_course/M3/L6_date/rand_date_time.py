import random
from datetime import datetime, timedelta

# Generate a random number of days and hours
days = random.randint(0, 365)
hours = random.randint(0, 23)

# Calculate random date and time
random_datetime = datetime.now() - timedelta(days=days, hours=hours)

print("Random Date and Time:", random_datetime)