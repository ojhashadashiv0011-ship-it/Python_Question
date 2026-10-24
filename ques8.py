# Question 8 — Count Even and Odd Numbers

numbers = [12, 7, 9, 20, 15, 8, 3]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers: ",even_count)
print("Odd numbers: ", odd_count)