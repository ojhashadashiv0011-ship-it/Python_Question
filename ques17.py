# Question 17 — Remove Duplicates


numbers = [4, 2, 4, 7, 2, 9, 7, 1]

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)