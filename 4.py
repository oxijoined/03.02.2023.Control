def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("Число четных чисел:", even_count)
    print("Число нечетных чисел:", odd_count)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count_even_odd(numbers)
