"""Asks for sum and gives amount of coins needed."""
sum = int(input("Enter a sum: "))
coins = 0

coins += sum // 50
sum = sum % 50

coins += sum // 20
sum = sum % 20

coins += sum // 10
sum = sum % 10

coins += sum // 5
sum = sum % 5

coins += sum

print(f"Amount of coins needed: {coins}")  # prints the result
