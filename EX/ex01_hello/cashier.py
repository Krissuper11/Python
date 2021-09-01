"""Asks for sum and gives amount of coins needed."""
sum = int(input("Enter a sum : "))  # reads input

# counts how many 50 cent coins
fifty_cent = sum // 50
left = sum - 50 * fifty_cent

# counts how many 20 cent coins
twenty_cent = left // 20
left = left - 20 * twenty_cent

# counts how many 10 cent coins
ten_cent = left // 10
left = left - ten_cent * 10

# counts how many 5 cent coins
five_cent = left // 5
left = left - five_cent * 5

one_cent = left   # all what left is 1 cent coin
amount = fifty_cent + twenty_cent + ten_cent + five_cent + one_cent  # counts amount of coins
print(f"Amount of coins needed: {amount}") # prints the result
