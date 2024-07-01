def count_e(string):
    count = 0
    
    for char in string:
        if char.lower() == 'e':
            count += 1
    
    print('Count of e :',count)
            

string = input('Enter the string:')
count_e(string)