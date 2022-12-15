print("Calculate my average grade")
amount = int(input("How many grades do u have!\n"))
grades = []
sum = 0

for n in range(1, amount + 1):
    grade = int(input(f"Grade {n}\n"))
    grades.append(grade)

for n in range(0, len(grades)):
    sum += grades[n]

avg = round(sum/amount, 2)
print(avg)