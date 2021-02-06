def create_phone_number(n):
    number_array = ['(', '0', '0', '0', ')', ' ', '0', '0', '0', '-', '0', '0', '0', '0']

    j = 0
    for i in range(len(number_array)):
        if number_array[i] == '0':
            number_array[i] = n[j]
            j += 1

    string_of_numbers = ""
    for number in number_array:
        string_of_numbers += str(number)

    return string_of_numbers


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
