# Question 13 — Find the Second Largest Number

numbers = [14, 27, 8, 45, 19, 32]


largest = 0
second_largest = 0
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest number:", second_largest)