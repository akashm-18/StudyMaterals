number = int(input('enter the number :' ))

odd_sum = 0

while number > 0 :
    last_digit = number % 10
    if last_digit % 2 != 0:
        odd_sum = odd_sum + last_digit
    number = number // 10

print(odd_sum)