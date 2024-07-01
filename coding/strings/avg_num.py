array = []

for i in range(1,6):
    array.append(int(input(f'Enter the {i}st Number : ')))
    
total = sum(array)

average = total / len(array)

print('Average of Numbers in the Array is ',average)