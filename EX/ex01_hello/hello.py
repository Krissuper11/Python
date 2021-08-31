"""asks input and gives results"""
name = input("What is your name? ")
arv1 = int(input("Hello, " + name + "! Enter a random number: "))
arv2 = int(input("Great! Now enter a second random number: "))
print(str(arv1) + " + " + str(arv2) + " is " + str(arv2 + arv1))

first_word = input("Roses are ..., ")
second_word = input("... are blue, ")
third_word = input("I love to ...")
print("And so will you!\n")
print("Roses are " + first_word + ",\n" + second_word + " are blue,\n" + "I love to " + third_word + "\nAnd so will "
                                                                                                     "you!")

greeting = input("Enter a greeting: ")
recipient = input("Enter a recipient: ")
number = int(input("How many times to repeat: "))
print((greeting + " " + recipient + "! ") * number)
