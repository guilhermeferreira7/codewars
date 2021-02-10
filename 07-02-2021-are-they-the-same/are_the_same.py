def comp(array1, array2):

    print(array1)
    print(array2)

    if (array1 is None) or (array2 is None) or (len(array1) != len(array2)):
        return False

    a_sorted = sorted(array1)
    b_sorted = sorted(array2)

    for i in range(len(array1)):
        if a_sorted[i] ** 2 != b_sorted[i]:
            return False

    return True
