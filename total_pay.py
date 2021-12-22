hrs = input("Enter Hours:")
rph = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rph)
except:
    print("Error. Need numeric input. Please try again.")
    print("End program.")
    quit()

if h <= 40:
    result = h * r
else:
    reg_pay = 40 * r
    ot_pay = (h - 40) * (r * 1.5)
    result = reg_pay + ot_pay

print(result)
