# 🐍 Question 6 — Find the Largest Number

numbers = [14, 27, 8, 45, 19, 32]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)
