from datetime import datetime

#get user input
target_event_year = int(input("Enter the year of the event: "))
target_event_month = int(input("Enter the month of the event: "))
target_event_day = int(input("Enter the day of the event: "))

#format date from user input
target_date = f"{target_event_year}-{target_event_month}-{target_event_day}"

#count days left
def get_days_from_today(date):
    now = datetime.today()

    try:
        planned_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None

    days_left = (planned_date - now).days

    return days_left

print("Days left:", get_days_from_today(target_date))