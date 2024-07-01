string = input('Enter the String : ')

count = 0

for char in string:
    if 48 <= ord(char) <= 57:
        count += 1 

print('No.of Number in string : ',count)