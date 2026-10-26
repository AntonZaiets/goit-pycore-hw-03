from datetime import datetime

#get user input
target_event_year = int(input("Enter the year of the event: "))
target_event_month = int(input("Enter the month of the event: "))
target_event_day = int(input("Enter the day of the event: "))

#format date from user input
target_date = f"{target_event_year}-{target_event_month}-{target_event_day}"

#count days left
def get_days_from_today(date):
    try:
        planned_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None

    today = datetime.today().date()

    return (today - planned_date).days

print("Days left:", get_days_from_today(target_date))