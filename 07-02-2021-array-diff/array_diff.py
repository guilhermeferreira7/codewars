def array_diff(a, b):
    result = []
    for elem in a:
        if elem not in b:
            result.append(elem)

    return result


