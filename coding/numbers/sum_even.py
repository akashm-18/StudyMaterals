def check_even(Digit):
    if Digit % 2 == 0:
        return True
    else:
        return False

number = int(input('Enter the Number : '))
even_sum = 0

while number > 0 :
    last_digit = number % 10
    evendigit = check_even(last_digit)
    if evendigit :
        even_sum = even_sum + last_digit
    number = number // 10

print('Sum of Even Digit : ',even_sum)
    