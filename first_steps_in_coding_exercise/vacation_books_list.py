pages_count = int(input())

pages_per_hous = int(input())

read_due_days = int(input())

book_reading_hours = pages_count / pages_per_hous

hours_rer_day = book_reading_hours / read_due_days

print(round(hours_rer_day))