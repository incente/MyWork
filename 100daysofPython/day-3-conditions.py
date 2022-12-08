#1. Nested conditions

#1.1 BMI calculator
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight / height**2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")

#1.1 Leap year
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

#2. Multiple If statements
age = int(input("What is your age? "))
bill = 0

if age < 12:
    bill = 4
elif age < 18:
    bill = 7
else:
    bill = 12

photo = input("Do you want a photo taken? Yes or No? ")

if photo == "Yes":
    bill += 3
    print(f"Your ticket price is {bill}.")
else:
    print(f"Your ticket price is {bill}.")

#3. Logical operators

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

both_names = (name1 + name2).lower()

true_l = int(both_names.count("t")) + int(both_names.count("r")) + int(both_names.count("u")) + int(both_names.count("e"))

t_love = int(both_names.count("l")) + int(both_names.count("o")) + int(both_names.count("v")) + int(both_names.count("e"))

true_love = str(true_l) + str(t_love)

true_love_int = int(true_love)

if true_love_int < 10 or true_love_int > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love_int > 40 and true_love_int < 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}")
