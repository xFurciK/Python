print("Calculating Body Mass Index (BMI)")
height=float(input("Enter your height in cm: "))
weight=float(input("Enter yout weight in kg: "))
BMI=(weight)/((height/100)**2)
#
print(f"BMI index: {BMI}")