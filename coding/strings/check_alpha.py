string = input('Enter the String : ')

count = 0

for char in string :
    if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 :
        count += 1

print('No.of Alpha : ',count)