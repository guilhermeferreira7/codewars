def create_array_of_tiers(n):

    array_of_numbers = list(str(n))
    string_aux = ''

    for i in range(len(array_of_numbers)):
        array_of_numbers[i] = string_aux + array_of_numbers[i]
        string_aux = array_of_numbers[i]

    return array_of_numbers


print(create_array_of_tiers(1357))
