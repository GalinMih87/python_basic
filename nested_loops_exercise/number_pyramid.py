number = int(input())
counter = 1
all = False

for row in range(1, number + 1):
    for colunn in range(1, row + 1):
        print(counter, end= " ")
        counter += 1
        if counter > number:
            all = True
            break
    if all:
        break
    print()