number_of_string = int(input())

for string in range(number_of_string):
    text = input()
    if "," in text or "." in text or "_" in text:
        print(f"{text} is not pure!")
    else:
        print(f"{text} is pure.")
