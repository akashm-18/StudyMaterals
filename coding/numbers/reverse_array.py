array = []

for i in range(1,6) :
    array.append(int(input(f'Enter the {i}st Number in the array : ')))
    
left = 0
right = len(array) - 1

while left <= right :
    array[left] , array[right] = array[right] , array[left]
    left += 1
    right -= 1
    
print('Reversed Array : ', array)