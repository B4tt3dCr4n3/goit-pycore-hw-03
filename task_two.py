""" Task 2: Write a function that generates a list of unique and sorted random numbers 
for a lottery ticket."""

import random

def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> list[int]:
    """This function generates a list of unique and sorted random numbers for a lottery ticket."""
    numbers = set() # Use a set to store unique numbers
    if max_val - min_val + 1 < quantity: # Check if the quantity is larger than the range of numbers
        print("Error: Quantity is larger than the range of numbers or equal!")
        return sorted(numbers) # Return an empty list if the quantity is too large
    if not 1 <= min_val <= max_val <= 1000: # Check if the input values are within the specified range
        print("Error: Invalid input. Ensure 1 <= min <= max <= 1000!")
        return sorted(numbers) # Return an empty list if the input values are invalid
    while len(numbers) < quantity: # Generate unique random numbers
        numbers.add(random.randint(min_val, max_val))
    return sorted(numbers) # Return the sorted list of unique numbers

# Test the function
lottery_numbers = get_numbers_ticket(1, 49, 6)  # Generate 6 numbers between 1 and 49
print("Your lottery numbers:", lottery_numbers) # Output: Your lottery numbers: [4, 12, 20, 23, 31, 42]
