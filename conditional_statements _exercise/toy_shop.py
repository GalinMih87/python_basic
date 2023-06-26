price_of_the_trip = float(input())
number_of_puzzles = int(input())
number_of_talking_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

price_of_puzzles = 2.6
price_of_talking_dolls = 3
price_of_teddy_bears = 4.1
price_of_minions = 8.2
price_of_trucks = 2

toys_price = number_of_puzzles * price_of_puzzles + number_of_talking_dolls * price_of_talking_dolls + \
      number_of_teddy_bears * price_of_teddy_bears + number_of_minions * price_of_minions + \
      number_of_trucks * price_of_trucks

numb_of_toys = number_of_puzzles + number_of_talking_dolls + number_of_teddy_bears + number_of_minions + number_of_trucks

if numb_of_toys >= 50:
    toys_price -= toys_price * 0.25

rent = toys_price * 0.1
income = toys_price - rent

money_left = round(income - price_of_the_trip, 2)

if money_left < 0:
    print(f"Not enough money! {abs(money_left):.2f} lv needed.")
else:
    print(f'Yes! {money_left:.2f} lv left.')
