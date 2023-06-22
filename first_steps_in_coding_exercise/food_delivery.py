chiken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

chiken_menu_price = chiken_menu * 10.35
fish_menu_price = fish_menu * 12.40
vegan_menu_price = vegan_menu * 8.15

price_for_all_menu = chiken_menu_price + fish_menu_price + vegan_menu_price
dessert_price = 0.2 * price_for_all_menu
delivery_price = 2.5

total_price = price_for_all_menu + dessert_price + delivery_price

print(total_price)



