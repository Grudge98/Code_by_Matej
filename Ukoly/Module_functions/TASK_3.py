def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def prime_count(numbers):
    count = 0
    for number in numbers:
        if is_prime(number):
            count += 1
    return count


numbers = [2, 3, 5, 20, 30, 15, 7, 9, 13]
result = prime_count(numbers)
print(result)