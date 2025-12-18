def unique_pair_sum(numbers, target):
    result = set()

    # Parcurgem lista cu doua for-uri
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            a = numbers[i]
            b = numbers[j]

            # Verificam suma si conditia a <= b
            if a + b == target and a <= b:
                result.add((a, b))

    return result


# Exemplu de test
numbers = [1, 2, 3, 4, 3, 5, 6]
target = 7
print(unique_pair_sum(numbers, target))
