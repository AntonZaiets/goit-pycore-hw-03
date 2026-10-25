import random

#read int
def read_int(placeholder):
    try:
        return int(input(placeholder))
    except ValueError:
        return None

#get user input
min_num = read_int("Enter the minimum number: ")
max_num = read_int("Enter the maximum number: ")
quantity_num = read_int("Enter the quantity number: ")

#validate user input
def validate_ticket_params(min, max, quantity):
    if not isinstance(min, int) or not isinstance(max, int) or not isinstance(quantity, int):
        return "All parameters must be integers."
    if min < 1:
        return "Minimum number must be at least 1."
    if max > 1000:
        return "Maximum number must be at most 1000."
    if min > max:
        return "Minimum number must not exceed maximum number."
    if not 1 <= quantity <= max - min + 1:
        return "Quantity must be between 1 and the size of the range."
    return None

#get random numbers
def get_numbers_ticket(min, max, quantity):
    error = validate_ticket_params(min, max, quantity)

    if error:
        print(error)
        return []

    pool_nums = list(range(min, max + 1))
    random_nums = random.sample(pool_nums, quantity)
    sorted_nums = sorted(random_nums)

    return sorted_nums

print(get_numbers_ticket(min_num, max_num, quantity_num))