#1. Loops
#1.1 For loops
friuts = ["apple", "banana", "grape"]
length = 0
for fruit in friuts:
    length += 1

#1.2 Average height
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

result = 0
for n in range(0, len(student_heights)):
    result += student_heights[n]

avg = round(result / len(student_heights))

# 1.3 Highest and lowest score
student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

max(student_scores)

highest = 0
for n in range(0, len(student_scores)):
    if student_scores[n] > highest:
        highest = student_scores[n]

min(student_scores)

#1.4 Range()
sum = 0
for n in range(1, 101):
    sum += n

print(sum)

#1.5 Add even numbers
sumEven = 0
for n in range(1, 101):
    if n % 2 == 0:
        sumEven += n

print(sumEven)