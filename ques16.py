# Bina min() function use kiye, list ka sabse chhota number find kar.

numbers = [14, 5, 28, 11, 36, 9]
smallest_num = numbers[0]
for num in numbers:
    if num < smallest_num:
        smallest_num = num
print(smallest_num)