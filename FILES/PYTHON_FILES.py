# USING "w"
# file = open("newfile.txt", "w")
# file.write("Line 1")
# file.close()
# USING "a"
# file = open("newfile.txt", "a")
# file.write("\nLine 3")
# file.close()
#  USING "w"
# file = open("newfile.txt", "w")
# file.write("Line 1 \nLine 2")
# file.close()
#  USING "r"
# file = open("newfile.txt", "r")
# content = file.read()
# file.close()
# print(content)
# a = ["Cat", "Dog", "Sheep", "Wolf"]
# file = open("ANIMAL.txt", "a")
# for x in a:
#     file.write(f"{x} \n")
# file.close()
def result():
    file = open("RESULT.txt", "a")
    name = input("Enter your name: ")
    gender = input("MALE/FEMALE : ")
    weight = int(input("Enter your weight in kilograms : "))
    height = int(input("Enter your height in meters : "))
    BMI = (weight/(height*height))
    if BMI >= 0 and BMI <= 18:
        BMIr = "underweight"
    elif BMI > 18 and BMI <= 25:
        BMIr = "normal"
    elif BMI > 25:
        BMIr = "overweight"
    else:
        BMIr = "invalid BMI"

    file.write(f"NAME: {name.upper()}\n")
    file.write(f"GENDER: {gender.upper()}\n")
    file.write(f"WEIGHT: {weight}kg\n")
    file.write(f"HEIGHT: {height}m\n")
    file.write(f"BODY MASS INDEX (BMI): {BMI}\n")
    file.write(f"BMI STATUS: {BMIr}\n")
    file.write(f"**********************************************\n")
    ans = input("Do you wish to enter another record, Y/N: ")
    if ans.upper() == "Y":
        result()
    else:
        print("Thank you and goodbye!")
    file.close()
with open("RESULT.txt", "a") as file:
    file.write("****************PATIENTS RECORDS************** \n")
result()

