# Question 11 — Count Numbers Greater Than Target 🔢

numbers = [12, 25, 7, 40, 18, 9, 35]
target = 20
count = 0
for num in numbers:
    if num > target:
        # target = count
        count += 1
        
print(count)