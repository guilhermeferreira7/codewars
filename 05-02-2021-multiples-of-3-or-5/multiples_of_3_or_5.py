def solution(number):
    total = 0

    if number > 0:
        for i in range(number - 1, 0, -1):
            if (i % 3 == 0) or (i % 5 == 0):
                total += i
    else:
        return 0

    return total


print(solution(10))


