#FLOW CHART DRAWING !!!
import random

wordList = ["morning", "noon", "afternoon", "evening", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
empty = []
end = False
lives = 5

word = random.choice(wordList) #random.choice with lists
print(f"Word is {word}")
for n in range(0, len(word)):
    empty.append("_")


while end != True:

    guess = input("Guess a letter: ").lower()
    not_equal = 0

    for n in range(0, len(word)):

        if word[n] == guess:
            empty[n] = guess
        
            print("".join(empty))

        else:
            not_equal += 1

            if not_equal == len(word):
                lives -= 1
                print(f"Oh no, wrong letter. You have {lives} left!")

                if lives == 0:
                    end = True
                    print("You lose!")
                    
    if "".join(empty) == word:
        end = True
        print("You win!")



    