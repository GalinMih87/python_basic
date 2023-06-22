nylon_price = 1.50
paint_price = 14.50
paint_thinner_price = 5.00

nylon_quantity = int(input())
paint_qualitity = int(input())
paint_thinner_quantity = int(input())
working_hours = int(input())

sum_nylon_price = (nylon_quantity + 2) * nylon_price
sum_paint_peice = (paint_qualitity + (paint_qualitity * 10/100)) * paint_price
sum_paint_thinner_price = paint_thinner_quantity * paint_thinner_price

supplies_price_sum = sum_nylon_price + sum_paint_peice + sum_paint_thinner_price + 0.40

workers_price = (supplies_price_sum * (30/100)) * working_hours

price_sum = supplies_price_sum + workers_price

print(price_sum)
