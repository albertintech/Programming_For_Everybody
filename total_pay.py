hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter rate:")
r = float(rph)

if h <= 40:
    result = h * r
else:
    reg_pay = 40 * r
    ot_pay = (h - 40) * (r * 1.5)
    result = reg_pay + ot_pay

print(result)
