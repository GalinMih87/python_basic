from datetime import date
n1 = input()
n2 = input()
d0 = date(2022, 8 , 18)
d1 = date(1987, 7 , 24)
difference1 = abs(d1 - d0)
#print(difference1.days)

d3 = date(2022, 8 , 18)
d4 = date(1987, 4 , 14)
difference2 = abs(d4 - d3)
#print(difference2.days)

difference3 = abs(difference2.days - difference1.days)
print(f"{n1} е по-дърта от {n2} с {difference3} дни.")