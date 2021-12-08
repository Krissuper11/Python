import random
n = 3
list2 = ["danja", "kristina", "kristofer", "olja"]
list3 = []
while True:
    input1 = input("Name: ")
    if input1 == "end":
        print(set(list3))
    index2 = random.randint(0, n)
    person2 = list2[index2]
    list3.append(person2)
    if person2 != input1:
        del list2[index2]
        print(person2)
        n -= 1
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")