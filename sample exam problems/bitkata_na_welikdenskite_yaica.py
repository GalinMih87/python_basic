first_player_eggs = int(input())
second_player_eggs = int(input())

line_inpust = input()

while line_inpust != "End of battle":
    if  line_inpust == "one":
        second_player_eggs -= 1
    elif line_inpust == "two":
        first_player_eggs -= 1

    if first_player_eggs == 0 or second_player_eggs == 0:
        break

    line_inpust = input()

if first_player_eggs == 0:
    print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
elif second_player_eggs == 0:
    print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
else:
    print(f"Player one has {first_player_eggs} eggs left.")
    print(f"Player two has {second_player_eggs} eggs left.")

