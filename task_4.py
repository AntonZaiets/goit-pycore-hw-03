from datetime import datetime, timedelta

#mock data
user_data = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.10.25"}
]

#constants
DAYS_IN_WEEK = 7
SATURDAY = 6

#move date from weekend to next monday
def shift_from_weekend(date):
    iso_day = date.isoweekday()
    if iso_day >= SATURDAY:
        date += timedelta(days=(DAYS_IN_WEEK - iso_day + 1))
    return date

def get_upcoming_birthdays(users):
    birthdays = []
    today_date = datetime.today().date()

    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        congratulation_date = shift_from_weekend(user_birthday.replace(year=today_date.year))

        #check if birthday is already passed this year
        if congratulation_date < today_date:
            congratulation_date = shift_from_weekend(user_birthday.replace(year=today_date.year + 1))

        #check if birthday is in next week
        if (congratulation_date - today_date).days <= DAYS_IN_WEEK:
            birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return birthdays

print(get_upcoming_birthdays(user_data))