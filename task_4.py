from datetime import datetime, timedelta

#mock data
user_data = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.10.25"}
]

#constants
DAYS_IN_WEEK = 7
SATURDAY = 6

def get_upcoming_birthdays(users):
    birthdays = []
    today_date = datetime.today().date()

    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        congratulation_date = user_birthday.replace(year=today_date.year)

        #check if birthday is already passed this year
        if congratulation_date < today_date:
            congratulation_date = congratulation_date.replace(year=today_date.year + 1)

        #check if birthday is in next week
        if (congratulation_date - today_date).days <= DAYS_IN_WEEK:
            iso_day = congratulation_date.isoweekday()
            if iso_day >= SATURDAY:
                congratulation_date += timedelta(days=(DAYS_IN_WEEK - iso_day + 1))

            birthdays.append({
                "name": user['name'],
                "congratulation_date": congratulation_date.strftime('%Y.%m.%d')
            })

    return birthdays

print(get_upcoming_birthdays(user_data))