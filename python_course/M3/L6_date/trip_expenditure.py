from datetime import datetime

def trip_expenditure(start_date, end_date, daily_expense):
    days = (end_date - start_date).days
    return days * daily_expense

# Main program
start = input("Enter start date (YYYY-MM-DD): ")
end = input("Enter end date (YYYY-MM-DD): ")
daily = float(input("Enter daily expense: "))

start_date = datetime.strptime(start, "%Y-%m-%d")
end_date = datetime.strptime(end, "%Y-%m-%d")

total = trip_expenditure(start_date, end_date, daily)

print("Number of days:", (end_date - start_date).days)
print("Total trip expenditure:", total)