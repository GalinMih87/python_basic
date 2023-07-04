import sys

max_number = -sys.maxsize
command = input()
while command != 'Stop':
    curent_number = int(command)
    if curent_number > max_number:
        max_number = curent_number
    command = input()
if max_number != -sys.maxsize:
    print(max_number)
