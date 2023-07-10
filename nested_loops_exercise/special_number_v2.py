number = int(input())
for curren_number in range(1111, 9999 + 1):
    number_is_special = True
    curren_number_as_string = str(curren_number)
    if "0" in curren_number_as_string:
        continue
    for curren_digit in curren_number_as_string:
        if int(curren_digit) == 0 or number % int(curren_digit) != 0:
            number_is_special = False
            break
    if number_is_special:
        print(curren_number_as_string, end=" ")