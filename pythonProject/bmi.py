#bmi


height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilograms: "))
bmi = weight / (height * height)
rounded_bmi = round(bmi, 2)
print("Your body mass index is: ", rounded_bmi)


