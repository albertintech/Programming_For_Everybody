
str_score = input("Enter score between 0.0 and 1.0: ")

try:
    score = float(str_score)
except:
    print("Error. Need numeric input. Please try again.")
    print("End program.")

if score < 0.0 or score > 1.0:
    print("Score out of range. Try again")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")  

