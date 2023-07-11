days = int(input())
available_food = float(input())

biscuit_total = 0
total_food = 0
dog_total_food = 0
cat_total_food = 0


for i in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    daily_food = dog_food + cat_food

    if i % 3 == 0:
        biscuit_total = biscuit_total + (0.1 * daily_food)

    total_food = total_food + daily_food

    dog_total_food = dog_total_food + dog_food
    cat_total_food = cat_total_food + cat_food

precent_tota = total_food / available_food * 100
precent_dog = dog_total_food / total_food * 100
precent_cat = cat_total_food / total_food * 100

print(f"Total eaten biscuits: {round(biscuit_total)}gr.")
print(f"{precent_tota:.2f}% of the food has been eaten.")
print(f"{precent_dog:.2f}% eaten from the dog.")
print(f"{precent_cat:.2f}% eaten from the cat.")


