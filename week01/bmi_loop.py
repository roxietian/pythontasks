# BMI Calculator for multiple people
# 1. ask how many people
n = int (input("Enter the number of people:"))
# 2. loop for each person
for i in range(n):
    print(f"\nPerson {i+1}:")
    height = float(input("Enter height(m):"))
    weight = float(input("Enter weight(kg):"))
    bmi = weight / (height**2)
    print(f"Person {i+1}'s bmi is: {bmi:.2f}")
    if bmi < 18.5:
        print("BMI Category: Underweight")
    elif 18.8 <= bmi < 25:
        print("BMI Category: Normal")
    elif 25 <= bmi < 30:
        print("BMI Category: Overweight")
    else:
        print("BMI Category: Obese")