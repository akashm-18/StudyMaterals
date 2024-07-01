string = input("Enter the String ")

vowel_count = 0
consonants_count = 0

for char in string :
    if char == 'a' or char == 'A' or char == 'e' or char == 'E' or char == 'i' or char == 'I' or char == 'o' or char == 'O' or char == 'u' or char == 'U' :
        vowel_count += 1
    else :
        consonants_count += 1
        
print('Vowels Count : ',vowel_count)
print('Consonants count : ', consonants_count)  
