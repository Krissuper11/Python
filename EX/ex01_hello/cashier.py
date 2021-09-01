"""Asks for sum and gives amount of coins needed."""
sum = int(input("Enter a sum: "))  # reads input

# counts how many 50 cent coins and what remains
fifty_cent = sum // 50
left = sum % 50

# counts how many 20 cent coins and what remains
twenty_cent = left // 20
left = left % 20

# counts how many 10 cent coins and what remains
ten_cent = left // 10
left = left % 10

# counts how many 5 cent coins and what remains
five_cent = left // 5
left = left % 5

amount = fifty_cent + twenty_cent + ten_cent + five_cent + left  # counts amount of coins
print(f"Amount of coins needed: {amount}")  # prints the result
