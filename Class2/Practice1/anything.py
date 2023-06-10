def print_hello():
    return "Hello world"


def print_given(data):
    return data


def sum_of_numbers(number_to_sum):
    total = 0
    string_number_to_sum = str(number_to_sum)
    for char in string_number_to_sum:
        total += int(char)

    return total
