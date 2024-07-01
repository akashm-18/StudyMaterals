string = input('Enter the String : ')
string = list(string)

left = 0
right = len(string) - 1

while left <= right :
    string[left] , string[right] = string[right] , string[left]
    left += 1
    right -= 1

reversed_string = ''.join(string)

print(reversed_string)