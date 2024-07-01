number = int(input('Enter the Number : '))

num1 = 0
num2 = 1
next_number = num2
count = 1

while count <= number :
    print(next_number,end=' ')
    num1 , num2 = num2 , next_number
    next_number = num1 + num2
    count += 1