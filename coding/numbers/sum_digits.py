number = int(input('Enter the number :'))

digit_sum = 0

while number > 0 :
    last_digit = number % 10
    digit_sum = digit_sum + last_digit
    number = number // 10
    
print('Total of Digits : ',digit_sum)