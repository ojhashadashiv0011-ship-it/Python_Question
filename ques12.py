# Question 12 — Sum of Numbers Greater Than Target

numbers = [12, 25, 7, 40, 18, 9, 35]
target = 20
sum = 0
for num in numbers:
    if num > target:
        sum = sum + num
        
        
print(sum)
