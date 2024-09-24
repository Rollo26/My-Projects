hieght = float(input("Enter your hieght in meters: ")) 
weight = float(input("Enter your wieght in kg: "))
hieght = hieght/100

bmi = weight/(hieght*hieght)
BMI = '%.2f' % bmi

print(F"Your Body mass index is: {BMI}")

if bmi > 0:
    if bmi <= 20:
        print("You are really underweight")
    elif bmi <= 22.5:
        print("You are underweight")
    elif bmi <= 29.5:
        print("You are healty")
    elif bmi <= 32:
        print("You are overweight")
    else:
        print("You are really overweight")
else:
    print("Please enter correct details")