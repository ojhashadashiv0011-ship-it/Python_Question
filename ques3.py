# Question 3 — Odd Numbers ka Sum

numbers = [12, 7, 9, 20, 15, 8]
sum = 0
for num in numbers:
    if num % 2 != 0:
        sum = sum + num
print(sum)