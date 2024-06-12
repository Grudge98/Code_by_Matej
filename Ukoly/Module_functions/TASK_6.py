def power_elements(list, power_number):
    return [x ** power_number for x in list]


numbers = [1, 2, 3, 4, 5, 6]
power = 3

powered_numbers = power_elements(numbers, power)
print(f"The powered list is: {powered_numbers}")