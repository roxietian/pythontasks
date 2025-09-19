height = float(input("Enter your height(m):"))
weight = float(input("Enter your weight(kg):"))
bmi = weight / (height**2)
print(f"Your bmi is: {bmi:.2f}")

if bmi < 18.5:
    print("BMI Category: Underweight")
elif 18.8 <= bmi < 25:
    print("BMI Category: Normal")
elif 25 <= bmi < 30:
    print("BMI Category: Overweight")
else:
    print("BMI Category: Obese")