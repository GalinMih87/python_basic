first_string = input()
second_string = input()
last_string = first_string

for symbol_index in range(len(second_string)):
    leeft_part = second_string[:symbol_index + 1]
    right_part = first_string[symbol_index + 1:]
    curent_string = leeft_part + right_part
    if curent_string == last_string:
        continue
    print(curent_string)
    last_string = curent_string

