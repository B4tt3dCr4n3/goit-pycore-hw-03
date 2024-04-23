"""Task 1: Write a function that takes a date as input and returns the number of days 
between the current date and a given date."""

from datetime import datetime

def get_days_from_today(date: str) -> int:
    """This function calculates the number of days between the current date and a given date.""" 
    try:
        date_format = "%Y-%m-%d"
        date_obj = datetime.strptime(date, date_format)
    except ValueError:
        return "Invalid date format. Please provide a date in 'YYYY-MM-DD' format."

    today = datetime.today()
    return (today - date_obj).days

# Test the function
print(get_days_from_today("2024-04-25")) # Output: -2
print(get_days_from_today("2024-04-01")) # Output: 22
print(get_days_from_today("24-04-25")) # Output: "Invalid date format. Please
# provide a date in 'YYYY-MM-DD' format."
