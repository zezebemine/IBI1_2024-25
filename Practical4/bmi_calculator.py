# Input your weight in kg
weight=float(input("enter your weight in kg:"))
# Input your height in m
height=float(input("enter your height in m:"))
# Calculate the BMI value by the formula
BMI=weight/height**2
# Compare your BMI value with two critical values to judeg whether your BMI is normal or not.
if BMI>30:
    print("obese")
elif BMI<18.5:
    print("underweight")
else:
    print("normal weight")