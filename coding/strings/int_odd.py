number = int(input('Enter the Number : '))

last_digit = number % 10

if last_digit == 0:
    print('Its Even Number')
elif last_digit % 2 == 0 :
    print('Its Even Number')
else:
    print('Its Odd Number')