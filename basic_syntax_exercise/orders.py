number_of_orders = int(input())
total_price = 0

for orders in range(number_of_orders):
    capsule_number = float(input())
    days = int(input())
    need_capsules_per_day = int(input())
    if capsule_number < 0.01 or capsule_number > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif need_capsules_per_day < 1 or need_capsules_per_day > 2_000:
        continue
    capsule_price = capsule_number * days * need_capsules_per_day
    total_price += capsule_price
    print(f"The price for the coffee is: ${capsule_price:.2f}")
print(f"Total: ${total_price:.2f}")


