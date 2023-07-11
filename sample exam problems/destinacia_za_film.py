buget = float(input())
destinacia = input()
sezon = input()
broi_dni = int(input())
price = 0

if sezon == "Winter":
    if destinacia == "Dubai":
        price = broi_dni * 45000
    elif destinacia == "Sofia":
        price = broi_dni * 17000
    elif destinacia == "London":
        price = broi_dni * 24000

if sezon == "Summer":
    if destinacia == "Dubai":
        price = broi_dni * 40000
    elif destinacia == "Sofia":
        price = broi_dni * 12500
    elif destinacia == "London":
        price = broi_dni * 20250

if destinacia == "Dubai":
    price -= price * 0.3
if destinacia == "Sofia":
    price += price * 0.25

diff = abs(buget - price)

if buget >= price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")

else:
    print(f"The director needs {diff:.2f} leva more!")
