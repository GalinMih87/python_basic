number_groups=int(input())
musala=0
monblan=0
kilimandjaro=0
k2=0
everest=0
total_members=0
for number in range(number_groups):
    group_members=int(input())
    total_members+=group_members
    if group_members<=5:
        musala+=group_members
    elif group_members<=12:
        monblan+=group_members
    elif group_members<=25:
        kilimandjaro+=group_members
    elif group_members<=40:
        k2+=group_members
    else:
        everest+=group_members
musala=musala/total_members*100
monblan=monblan/total_members*100
kilimandjaro=kilimandjaro/total_members*100
k2=k2/total_members*100
everest=everest/total_members*100
print(f'{musala:.2f}%')
print(f'{monblan:.2f}%')
print(f'{kilimandjaro:.2f}%')
print(f'{k2:.2f}%')
print(f'{everest:.2f}%')