word = input('enter the string : ')

count = 0

for char in word :
    if char == 'e' or char == 'E' :
        count = count + 1
        
print(count)