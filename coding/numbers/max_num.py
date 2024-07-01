array = []

for i in range(1,6):
    array.append(int(input(f'Enter the {i}st Number in the Array : ')))
    
max_number = array[0]

for i in range(len(array)):
    if array[i] > max_number :
        max_number = array[i]

print(max_number)