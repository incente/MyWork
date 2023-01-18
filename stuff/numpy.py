import random, numpy

def create_list():

    rand_list = []

    for _ in range(15):
        rand_num = random.randint(0, 1000)
        rand_list.append(rand_num)

    return rand_list

rand_list = create_list()

#Mean
list_mean = numpy.mean(rand_list)
print(f"Mean: {list_mean}")