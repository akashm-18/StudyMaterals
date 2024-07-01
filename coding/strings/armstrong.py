number = int(input('Enter the Number : '))

num = number
n = len(str(num))

sum = 0

while num > 0 :
    digit = num % 10
    sum += (digit ** n)
    num = num // 10

if sum == number :
    print('Yes , its an armstrong Number')
else:
    print('No , its Not an Armstrong Number')