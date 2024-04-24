"""Task 4: Write a function that takes a list of users with their names and birthdays and 
returns a list of upcoming birthdays within the next 7 days."""

from datetime import datetime

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """This function takes a list of users with their names and birthdays and
    returns a list of upcoming birthdays within the next 7 days."""
    upcoming_birthdays = []
    today = datetime.today().date()
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date() # Convert string to date
        birthday_this_year = birthday.replace(year=datetime.today().year) # Set the year to the current year
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=datetime.today().year + 1) # Set the year to the next year
        days_until_birthday = birthday_this_year - today # Calculate the days until the birthday
        if 0 <= days_until_birthday.days <= 7: # Check if the birthday is within the next 7 days
            while birthday_this_year.weekday() > 4: #
                birthday_this_year = birthday_this_year.replace(day=birthday_this_year.day + 1) 
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            }) # Add the user's name and the congratulation date to the list

    return upcoming_birthdays # Return the list of upcoming birthdays

users_list = [
    {"name": "John Doe", "birthday": "1985.04.27"}, # Saturday check, within 7 days
    {"name": "Jane Smith", "birthday": "1990.04.28"}, # Sunday check, within 7 days
    {"name": "Lavender Brown", "birthday": "1979.04.26"}, # Friday check, within 7 days
    {"name": "Parvati Patil", "birthday": "1988.04.24"}, # Today check
    {"name": "Harry Potter", "birthday": "1980.07.31"}, # Not within 7 days
    {"name": "Ron Weasley", "birthday": "1980.03.01"} # Not within 7 days
]

print(get_upcoming_birthdays(users_list)) # Output: [{'name': 'John Doe', 'congratulation_date': '2024.04.27'}, {'name': 'Jane Smith', 'congratulation_date': '2024.04.28'}, {'name': 'Lavender Brown', 'congratulation_date': '2024.04.26'}]
