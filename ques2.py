# Task: List mein se saare odd numbers ko "Odd" label ke saath print karo.

numbers = [12, 7, 9, 20, 15, 8]
for num in numbers:
    if num % 2 != 0:
        print("Odd", num)