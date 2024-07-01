def check_anagram(string1,string2):
    
    if len(string1) != len(string2) :
        raise ValueError ("Length of both needed to be Same")
    
    nums_map = {}
    
    for i in range(len(string1)):
        if string1[i] in nums_map:
            nums_map[string1[i]] += 1
        else :
            nums_map[string1[i]] = 1
    
    for j in range(len(string2)):
        if string2[j] in nums_map:
            nums_map[string2[j]] -= 1
        else:
            return False
    
    keys = nums_map.keys()
    
    for key in keys :
        if nums_map[key] != 0 :
            return False
        else:
            return True


string1 = input('Enter the First String : ')
string2 = input('Enter the Second String : ')

try :
    is_anagram = check_anagram(string1,string2)
    
    if is_anagram:
        print("Both are Anagram")
    else:
        print('Not an Anagram')

except ValueError as e :
    print(f"Some Error in Inputs : {e}")