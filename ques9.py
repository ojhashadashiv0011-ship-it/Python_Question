#  Question 9 — Reverse a List
numbers = [10, 20, 30, 40, 50]
reverse__list = []
for i in range(len(numbers)-1,-1,-1):
    reverse__list.append(numbers[i])
print(reverse__list)