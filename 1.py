# Более краткое решение
def calculate(shape: str, length: float) -> float:
    import math

    return [length * 4, 2 * math.pi * length][shape == "c"]


print(calculate("s", 5))
print(calculate("c", 5))
