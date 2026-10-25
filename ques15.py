# Bina max() function use kiye, list ka sabse bada number find karna hai.

numbers = [14, 5, 28, 11, 36, 9]
largest_num = 0
for num in numbers:
    if num > largest_num:
        largest_num = num
print(largest_num)