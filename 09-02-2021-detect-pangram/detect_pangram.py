import string


def is_pangram(s):
    lower_text = s.lower()
    string_list = sorted(list(lower_text))
    alphabet_list = list(string.ascii_lowercase)

    for letter in alphabet_list:
        if letter not in string_list:
            return False

    return True


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
