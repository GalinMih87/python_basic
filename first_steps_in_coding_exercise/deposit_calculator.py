depositet_amount = float(input())
pay_time = int(input())
annual_interest = float(input())

accrued_interest = depositet_amount * (annual_interest / 100)
interest_per_month = (accrued_interest / 12)
total = depositet_amount + (pay_time * interest_per_month)
formatted_total = round(total, 2)
print(formatted_total)
