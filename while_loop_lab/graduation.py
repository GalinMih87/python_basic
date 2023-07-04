student_name = input()
bad_tripies = 0
curent_class = 1
grade = 0
is_ejected = False

while curent_class <= 12:
    curent_grade = float(input())
    if curent_grade < 4:
        bad_tripies +=1
        if bad_tripies == 2:
            is_ejected = True
            break
        continue
    grade += curent_grade
    curent_class += 1

if is_ejected:
    print(f'{student_name} has been excluded at {curent_class} grade')
else:
    print(f'{student_name} graduated. Average grade: {grade / 12:.2f}')
