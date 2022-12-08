#1. String subscipting
"Hello world!"[11]
hello = "Hello wolrd!"
hello[len(hello)-1]

#1.1 Large integers
123_456_789

#1.2 Round float
round(17.123, 1)
int(17.123)

#1.3 Detect datatype
lenInp = len(input("What is your name?" ))
type(lenInp)

#1.4 Change datatype to string
lenInpStr = str(lenInp)
"Your name has " + lenInpStr + " characters."

#1.5 Change datatypes
70 + float("100.5")
int("123") + 123


#2. Operators
1 + 1
1 - 1
2 / 1
2 * 1
2 ** 3

#2.1 Use Result
score = 0
score += 1
score -= 1

#3. f-Strings
f"your score is {score}"

#4 Tip calculator
print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")
split = float(total) * (int(percentage)/100) / int(people)
string = f"Each person should pay: ${split}"
print(string)