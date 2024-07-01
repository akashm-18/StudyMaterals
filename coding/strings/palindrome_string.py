def check_palindrome(string):
    check_str = list(string)
    left = 0
    right = len(check_str) - 1
    
    while left <= right :
        check_str[left] , check_str[right] = check_str[right] , check_str[left]
        left += 1
        right -= 1
    
    checked_string = ''.join(check_str)
    if string == checked_string :
        return True
    else:
        return False



s = input('Enter the String : ')

if check_palindrome(s):
    print('The Given string is palidrome')
else:
    print('Not a palindrome')