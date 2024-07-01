def factoriol(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factoriol(number - 1)            # ------> Using Rescursion 


number = int(input('Enter the Number : '))
result = factoriol(number)
print(result)


# number = int(input('Enter the Number : '))

# result = 1
                                                    # ---> Without using Recursion Basic Apporach
# for i in range(1,number + 1) :
#     result = result * i

# print(result)    