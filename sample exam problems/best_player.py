from sys import maxsize
best_player_name = ''
best_player_scored = - maxsize

while True:
    player_name = input()
    if player_name == 'END':
        break
    scored_goals = int(input())

    if scored_goals > best_player_scored:
        best_player_name = player_name
        best_player_scored = scored_goals

    if scored_goals >= 10:
        break

print(f"{best_player_name} is the best player!")
if best_player_scored >= 3:
    print(f"He has scored {best_player_scored} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_scored} goals.")