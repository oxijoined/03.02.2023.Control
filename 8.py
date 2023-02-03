def find_even_numbers():
    result = []
    for i in range(100, 401):
        is_even = all(int(digit) % 2 == 0 for digit in str(i))
        if is_even:
            result.append(i)
    return result


print(*find_even_numbers(), sep=", ")
