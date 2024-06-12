def remove_number(list, number):
    count = 0
    while number in list:
        list.remove(number)
        count += 1
    return count


numbers = [3, 2, 5, 6, 8, 9, 4, 3, 2, 8, 3, 32]
number_to_remove = 3
removed = remove_number(numbers, number_to_remove)
print(f"removed {removed} numbers, the updated list is: {numbers}")