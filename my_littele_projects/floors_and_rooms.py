
floors = int(input())
rooms = int(input())
sum = 0
for f in range(floors, (-3),-1):
    for r in range(0, rooms):

        if f == floors:
            print(f"Ат. {f}{r}", end=' ')
        elif f == 0:
            print(f"Оф. {f}{r}", end=' ')
        elif f == -1:
            print(f"ПM {-f}{r}", end=' ')
        elif f == -2:
            print(f"ПM {-f}{r}", end=' ')
        else:
            print(f"Ап. {f}{r}", end=' ')

    print() # сваля курсора на нов ред