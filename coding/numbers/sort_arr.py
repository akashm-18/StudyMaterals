array = []

for i in range(1,6):
    array.append(int(input(f'Enter the {i}st Number in the Array : ')))         # ---> This is Called as the Bubble sort
    
for i in range(len(array)):
    for j in range(0,len(array) -i - 1) :
        if array[j] > array[j + 1] :
            array[j] , array[j + 1] = array[j + 1] , array[j]
            
print('Sorted Array ', array)