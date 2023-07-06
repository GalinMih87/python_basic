import sys

n = int(input())

nums_sum = 0
bigest_num = -sys.maxsize

for number in range(n):
    num = int(input())

    nums_sum += num

    if num > bigest_num:
        bigest_num = num

other_nums = nums_sum - bigest_num

if bigest_num == other_nums:
    print("Yes")
    print(f"Sum = {bigest_num}")
else:
    print("No")
    print(f"Diff = {abs(bigest_num - other_nums)}")




