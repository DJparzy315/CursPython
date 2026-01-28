import math


# Fibonacci iterativ (evitam recursia si memo default mutabil)
def fibonacci(n):
    if not isinstance(n, int):  # verificare tip
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):  # varianta iterativa, fara stack overflow
        a, b = b, a + b
    return b


# Aria cercului cu validare tip + valoare
def circle_area(radius):
    if not isinstance(radius, (int, float)):  # prevenim TypeError ascuns
        raise TypeError("Radius must be a number.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2


# Maxim iterativ (evitam recursie + copiere lista)
def find_max(numbers):
    if not isinstance(numbers, list):  # validare tip
        raise TypeError("Input must be a list.")
    if not numbers:
        raise ValueError("Cannot find the maximum of an empty list.")

    maximum = numbers[0]
    for num in numbers[1:]:  # O(n), fara slicing recursiv
        if num > maximum:
            maximum = num
    return maximum


# Media geometrica stabila numeric (folosim log)
def geometric_mean(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if not numbers:
        raise ValueError("Cannot calculate geometric mean of an empty list.")

    log_sum = 0
    count = 0

    for num in numbers:
        if not isinstance(num, (int, float)):  # verificare tip elemente
            raise TypeError("All elements must be numbers.")
        if num <= 0:
            raise ValueError("All numbers must be positive for geometric mean.")
        log_sum += math.log(num)  # evitam overflow la inmultiri mari
        count += 1

    return math.exp(log_sum / count)


def main():
    print("=== Fibonacci ===")
    n = 30
    try:
        print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
    except (ValueError, TypeError) as e:
        print(e)

    print("\n=== Circle Area ===")
    radius = -5
    try:
        print(f"The area of a circle with radius {radius} is: {circle_area(radius)}")
    except (ValueError, TypeError) as e:
        print(e)

    print("\n=== Find Max ===")
    numbers = []
    try:
        print(f"The maximum value in the list {numbers} is: {find_max(numbers)}")
    except (ValueError, TypeError) as e:
        print(e)

    print("\n=== Geometric Mean ===")
    numbers = [1, 2, 0, 4]
    try:
        print(f"The geometric mean of {numbers} is: {geometric_mean(numbers)}")
    except (ValueError, TypeError) as e:
        print(e)


# prevenim rularea automata la import
if __name__ == "__main__":
    main()
