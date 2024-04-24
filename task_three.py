"""Task 3: Write a function that normalize a phone number by removing certain 
characters and add a country code if necessary."""

import re

def normalize_phone(phone_number: str) -> str:
    """Normalize a phone number by removing certain characters and adding a 
    country code if necessary."""
    pattern = r"[()\\n\\t;,\-:!\.\\ ]" # Define the pattern to remove
    replacement = "" # Define the replacement
    phone_number = re.sub(pattern, replacement, phone_number) # Remove the characters

    if phone_number.startswith('0'): # Check if the number starts with 0
        phone_number = '+38' + phone_number # Add the country code

    elif phone_number.startswith('380'): # Check if the number starts with 380
        phone_number = '+' + phone_number # Add the country code
    return phone_number # Return the normalized phone number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


sanitized_numbers = [normalize_phone(phone_number) for phone_number in raw_numbers] # Normalize the phone numbers
print("Normalized phone numbers for SMS campaign:", sanitized_numbers) # Print the normalized phone numbers

# """Task 3: Write a function that normalize a list of phone numbers by removing 
# certain characters and adding a country code if necessary."""

# import re

# def normalize_phone(phone_numbers: list[str]) -> list[str]:
#     """Normalize a list of phone numbers by removing certain characters and adding a 
#     country code if necessary."""
#     sanitized_numbers = []
#     for phone_number in phone_numbers:
#         pattern = r"[()\\n\\t;,\-:!\.\\ ]"
#         replacement = ""
#         phone_number = re.sub(pattern, replacement, phone_number)

#         if phone_number.startswith('0'):
#             phone_number = '+38' + phone_number

#         elif phone_number.startswith('380'):
#             phone_number = '+' + phone_number
#         sanitized_numbers.append(phone_number)
#     return sanitized_numbers

# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# print("Normalized phone numbers for SMS campaign:", normalize_phone(raw_numbers))
