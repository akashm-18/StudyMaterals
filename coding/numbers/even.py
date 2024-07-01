number = int(input("Enter the Number : "))

even_sum = 0

while number > 0 :
    last_digit = number % 10
    if last_digit % 2 == 0:
        even_sum = even_sum + last_digit
    number = number // 10
    
print(even_sum)