def paint_letterboxes(start, finish):
    diff = (finish + 1) - start
    numbers = []

    for i in range(diff):
        numb_array = list(str(start))

        for number in numb_array:
            numbers.append(int(number))
        start += 1

    result = []
    for i in range(10):
        result.append(numbers.count(i))

    return result


print(paint_letterboxes(125, 132))
