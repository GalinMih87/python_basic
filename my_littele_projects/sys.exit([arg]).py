import sys

age = int(input())

if age < 18:
    sys.exit("Age less than 18")
else:
    print("Age is not less than 18")
    