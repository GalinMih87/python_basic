import sys

min_number = sys.maxsize
command = input()
while command != 'Stop':
    curent_number = int(command)
    if curent_number < min_number:
        min_number = curent_number
    command = input()
if min_number != sys.maxsize:
    print(min_number)