def digitize(n):
    array_of_numbers = list(str(n))
    result = []

    for i in range(len(array_of_numbers) - 1, -1, -1):
        result.append(int(array_of_numbers[i]))
    return result

