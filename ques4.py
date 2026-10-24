# Question 4 — Average of Numbers

numbers = [12, 7, 9, 20, 15, 8]
sum = 0
count = len(numbers)
average = 0
for num in numbers:
        sum = sum + num
        average = sum / count
print(average)