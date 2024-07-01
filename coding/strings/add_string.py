def add_string(number1,number2) :
    n1 = len(number1) - 1
    n2 = len(number2) - 1
    
    carry = 0
    ans = []
    
    while n1 >= 0 or n2 >= 0 :
        if n1 < 0 :
            ans.append(str( (int(number2[n2]) + carry ) % 10 ))
            carry = (int(number2[n2]) + carry ) // 10
            n2 -= 1
        elif n2 < 0 :
            ans.append(str((int(number1[n1]) + carry ) % 10 ))
            carry = (int(number1[n1]) + carry) // 10
            n1 -= 1
        else :
            ans.append(str( (int(number1[n1]) + int(number2[n2]) + carry) % 10 ))
            carry = ( int(number1[n1]) + int(number2[n2]) + carry ) // 10
            n1 -= 1
            n2 -= 1
        
    if carry :
        ans.append(str(carry))
        
    ans.reverse()
    
    return ''.join(ans)



number1 = input('Enter the Number String 1 : ')
number2 = input('Enter the Number String 2 : ')

result = add_string(number1,number2)
print(result)