#1. print multiple lines
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#1.1 \n to break lines
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")


#2. insert data with input function and return it
print("Hello " + input("What is your name? ") + "!")

#2.1 print length of inserted data
print(len(input("Whats your name? ")))

#2.2 save input data as variable and print it
name = input("Whats your name? ")
print(name)

#3. band name generator program
cityName = input("What's the name of the city you grew up in? ")
print(cityName)
petsName = input("What's your pet's name? ")
print(petsName)
bandName = cityName + " " + petsName
print("Your band name could be " + bandName)