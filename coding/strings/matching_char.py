def check_matching_char(string1,string2):
    
    non_matching = []
    
    if len(string1) != len(string2):
        raise ValueError ('Strings need to be same length')
    
    for char1 , char2 in zip(string1,string2):
        if char1 != char2:
            non_matching.append((char1,char2))

    return non_matching


first_string = input('Enter First String : ')
second_string = input('Enter Second String : ')


try :
    result = check_matching_char(first_string,second_string)
    
    if result :
        for char1 , char2 in result :
            print(f"{char1} in First String doesn't Match with {char2} in second string")
    else:
        print('Both Strings are Identical')

except ValueError as e :
    print(f'{e}')