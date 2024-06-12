def find_minimum(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum


numbers = [4, 6, 9, 2, 92, 23, -4, 34]
result = find_minimum(numbers)
print(result)