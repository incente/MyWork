#1. Try and exept
my_str = "This is a string"

try:
    my_str += 12
except:
    my_str = -1

print(my_str)

#1.1 Break and continue
for n in range(0, 10):
    if n % 2 == 0:
        continue
    print(n)

for n in range(0, 15):
    if n == 10:
        break
    print(n)

#1.2 Dictionarys
dictionary = {
    "mon": 12,
    "tue": 13,
    "wed": 14
}

dictionary["mon"] = 13
dictionary["tue"] = 14
dictionary["wed"] = 15
dictionary["fri"] = 17
