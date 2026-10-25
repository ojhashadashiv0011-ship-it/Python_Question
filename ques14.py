# Ye code likh, jo list ke saare even numbers ka sum calculate kare:

numbers = [12, 7, 9, 20, 15, 8]
even_sum = 0 
for num in numbers:
    if num % 2 == 0:
        even_sum = num + even_sum

print(even_sum)
