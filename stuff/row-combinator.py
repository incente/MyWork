import itertools, os


def permute(elements):
    permutations = list(itertools.permutations(elements))

    for permutation in permutations:
        print(permutation)

    return permutations


def students():
    student_list = []

    while True:

        try:
            amount = int(input("Amount students: "))

            for n in range(amount):
                student = input(f"Student {n + 1}: ")
                student_list.append(student)
            return student_list

        except ValueError:
            print("ERROR Amount must be an Integer")


def instruction(list, amount):
    while True:
        os.system('cls')
        command = input("Condition: ").split()
        result = []
        
        if command[2] == "neben":
            a = command[0] 
            b = command[len(command) - 1]

            for permutation in list:
                for n in range(amount):
                    if permutation[n] == a:
                        if n == 0:
                            if permutation[n + 1] == b:
                                result.append(permutation)
                        elif n == len(permutation) - 1:
                            if permutation[n - 1] == b:
                                result.append(permutation)
                        else:
                            if permutation[n - 1] == b or permutation[n + 1] == b:
                                result.append(permutation)

        elif command[2] == "links" or command[2] == "rechts" or command[2] == "linksmitte" or command[2] == "rechtsmitte":
            a = command[0]
            x = command[2]

            for permutation in list:
                if x == "rechtsmitte":
                    if permutation[len(permutation) - 2] == a:
                        result.append(permutation)
                elif x == "linksmitte":
                    if permutation[1] == a:
                        result.append(permutation)
                elif x == "links":
                    if permutation[0] == a:
                        result.append(permutation)
                elif x == "rechts":
                    if permutation[len(permutation) - 1] == a:
                        result.append(permutation)
                       
        for r in result:
            print(r)

        again = input("Type 'yes' for another condition: ")
        if again.lower() != "yes":
            break
        else:
            list = result

    return result
    

def start():
    student_list = students()
    amount = len(student_list)

    permutations = permute(student_list)
    for result in instruction(permutations, amount):
        print(result)
    again = input("Type 'yes' for again: ")
    if again.lower() == "yes":
        start()

start()