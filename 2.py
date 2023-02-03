def generate_fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


generate_fibonacci_sequence(50)
