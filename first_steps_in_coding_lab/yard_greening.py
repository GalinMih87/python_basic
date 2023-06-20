square_meters = float(input())

price = square_meters * 7.61
discount = price * 0.18
price_with_discount = price - discount

print(f'The final price is: {price_with_discount} lv.')
print(f'The discount is: {discount} lv.')