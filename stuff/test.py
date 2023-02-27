l1 = [1, 2, 5]
l2 = [2, 3, 4]


def test(l1, l2):
    for n in range(len(l2)):
        if l2[n] < l1[n]:
            return l2[n]
        
print(test(l1, l2))