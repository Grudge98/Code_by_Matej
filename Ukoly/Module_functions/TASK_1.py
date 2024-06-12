def product_of_elements(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product


numbers = [1, 2, 3, 4, 5, 8]
result = product_of_elements(numbers)
print(result)