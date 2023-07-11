start = int(input())
end = int(input())
magic_numb = int(input())

flag = False
count = 0
for i in range(start, end + 1):
    for j in range(start, end + 1):
        sum = i and j
        count += 1

        if sum == magic_numb:
            print(f"Combination N:{count}")
            flag = True
            break
    if flag:
        break

if not flag:
    print(f"Not in range!")