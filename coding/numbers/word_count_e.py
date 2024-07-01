string = input('Enter the String : ')

count = 0

for word in string:
    for char in word:
        if char.lower() == 'e':
            count += 1

print(count)