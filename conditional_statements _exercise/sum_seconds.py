
time_first = int(input())
time_second = int(input())
time_third = int(input())

seconds= time_first + time_second + time_third
minutes = 0
if seconds > 59:
    minutes += 1
    seconds = seconds - 60
if seconds > 59:
    minutes += 1
    seconds = seconds - 60
if seconds < 10:
   print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
