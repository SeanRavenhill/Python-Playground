import math

loan = 1000000
n = 60
i = 10

total_payments = 0

r = i / (12 * 100)
annuity = loan * ((r * ((1 + r) ** n)) / (((1 + r) ** n) - 1))
annuity = math.ceil(annuity)
total_payments += annuity * n

print(f"Your annuity payment = {annuity}!")

overpayment = int(total_payments - loan)

if overpayment > 0:
    print(f"Overpayment = {overpayment}")
