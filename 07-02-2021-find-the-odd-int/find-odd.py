def find_it(seq):
    sorted_list = sorted(seq)
    sorted_list.append('a')

    if (len(sorted_list) > 1) and (sorted_list[0] != sorted_list[1]):
        return sorted_list[0]

    counter = 0
    last = sorted_list[0]

    next_el = sorted_list[0]

    for i in range(len(sorted_list)):
        if i < len(sorted_list) - 1:
            next_el = sorted_list[i+1]

        if sorted_list[i] == last:
            counter += 1
        else:
            counter = 1

        if (counter % 2 == 1) and (sorted_list[i] != next_el):
            return sorted_list[i]

        last = sorted_list[i]
    return sorted_list[0]


print(find_it([1,1,1,1,1,1,10,1,1,1,1]))
