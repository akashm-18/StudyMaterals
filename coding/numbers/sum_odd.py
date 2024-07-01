def check_odd(digit):
    if digit % 2 != 0:
        return True
    else:
        return False
    
number = int(input('Enter the Number :'))

odd_sum = 0

while number > 0:
    last_digit = number % 10
    odddigit = check_odd(last_digit)
    if odddigit :
        odd_sum = odd_sum + last_digit
    number = number // 10
    
print('Odd sum is : ',odd_sum)