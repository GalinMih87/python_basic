flowers_type = input()
flowers_count = int(input())
buget = int(input())
final_price = 0

rosses_price = 5
dahlies_price = 3.8
tulips_price = 2.8
narcissus_price = 3
glagiolus_price = 2.5

if flowers_type == "Roses":
    final_price = rosses_price * flowers_count
    if flowers_count > 80:
        final_price -= final_price * 0.1

elif flowers_type == "Dahlias":
    final_price = dahlies_price * flowers_count
    if flowers_count > 90:
        final_price -= final_price * 0.15

elif flowers_type == "Tulips":
    final_price = tulips_price * flowers_count
    if flowers_count > 80:
        final_price -= final_price * 0.15

elif flowers_type == "Narcissus":
    final_price = narcissus_price * flowers_count
    if flowers_count < 120:
        final_price += final_price * 0.15

elif flowers_type == "Gladiolus":
    final_price = glagiolus_price * flowers_count
    if flowers_count < 80:
        final_price += final_price * 0.2
if buget >= final_price:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {buget - final_price:.2f} leva left.")
else:
   print(f'Not enough money, you need {final_price - buget:.2f} leva more.')