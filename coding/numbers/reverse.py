string = input('Enter the words : ')

i = 0
result = ''
n = len(string)

while i < n:
    while i < n and string[i] == ' ':
        i = i + 1
    if i >= n:
        break
    j = i + 1
    
    while j < n and string[j] != ' ':
        j = j + 1
    
    substring = string[i:j]
    i = j + 1

    if len(result) == 0:
        result = substring
    else:
        result = substring + ' ' + result
        
print(result)