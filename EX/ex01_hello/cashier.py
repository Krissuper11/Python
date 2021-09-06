"""Asks for sum and gives amount of coins needed."""
sum = int(input("Enter a sum: "))  # reads input
coins = 0

# counts how many 50 cent coins and what remains
coins += sum // 50
sum = sum % 50

# counts how many 20 cent coins and what remains
coins += sum // 20
sum = sum % 20

# counts how many 10 cent coins and what remains
coins += sum // 10
sum = sum % 10

# counts how many 5 cent coins and what remains
coins += sum // 5
sum = sum % 5

coins += sum  # counts how many 1 cent coins

print(f"Amount of coins needed: {coins}")  # prints the result
