number = int(input('Enter Number : '))

sum_of_digit = 0

while number > 0 :
    last_digit = number % 10
    sum_of_digit = sum_of_digit + last_digit
    number = number // 10
    
print(sum_of_digit)


# # digits = [1,2,3,4,5]

# # for num in digits:
# #     print(num)
    
# number = int(input('Enter the Number : '))

# for num in range(1,number+1):
#     print(num)
