height=float(input("Enter height:"))
weight=float(input("Enter weight:"))

BMI=weight/(height/100)**2

print("Your BMI is ",BMI)


if BMI<=18.4:
    print("You are underweight")
elif BMI<=24.9:
    print("You are healthy")
else:
    print("You are not healthy")