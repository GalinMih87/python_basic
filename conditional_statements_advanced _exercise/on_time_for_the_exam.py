exam_hour = int(input())
exam_min = int(input())
arrivel_hour = int(input())
arrivel_min = int(input())

exam_time = exam_min + exam_hour * 60
arrival_time = arrivel_min + arrivel_hour * 60
diff = exam_time - arrival_time

if diff < 0:
    print("Late")
    diff = abs(diff)
    if arrival_time != exam_time:
        hours = diff // 60
        minutes = diff % 60
        if hours > 0:
            print(f"{hours}:{minutes:02d} hours after the start")
        else:
            print(f'{minutes} minutes after the start')

elif diff <= 30:
    print("On time")
    if diff > 0:
        print(f'{diff} minutes before the start')

else:
    print('Early')
    if arrival_time != exam_time:
        hours = diff // 60
        minutes = diff % 60
        if hours > 0:
            print(f"{hours}:{minutes:02d} hours before the start")
        else:
            print(f'{minutes} minutes before the start')