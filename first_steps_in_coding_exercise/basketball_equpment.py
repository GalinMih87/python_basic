price_of_training_for_the_year = int(input())
price_on_basketball_sneakers = price_of_training_for_the_year - (price_of_training_for_the_year * 0.4)
price_on_basketball_outfit = price_on_basketball_sneakers - (price_on_basketball_sneakers * 0.20)
price_on_basketball_ball = price_on_basketball_outfit  / 4
price_on_basketball_accessories = price_on_basketball_ball / 5

total_price = price_of_training_for_the_year + price_on_basketball_sneakers + price_on_basketball_outfit + \
              price_on_basketball_ball + price_on_basketball_accessories

print(total_price)


