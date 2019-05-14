def my_function(numbers):
    sum = 0
    for number in numbers:
        if number % 2 != 0:
            sum += number
        else:
            continue
    return sum

print(my_function([11, 5, 1, 2, 4, 6]))