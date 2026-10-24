# Question 7 — Find the Smallest Number

numbers = [14, 27, 8, 45, 19, 32]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print(smallest)