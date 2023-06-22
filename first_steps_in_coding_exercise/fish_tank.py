length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percentage = float(input())

V_in_cm3 = length_in_cm * width_in_cm * height_in_cm
V_in_liters = V_in_cm3 / 1000
occupied_space = percentage / 100

need_liters = V_in_liters * (1 - occupied_space)

print(need_liters)


