array = []

for i in range(1,6):
    array.append(int(input(f'Enter the {i}st Number in array : ')))

target = int(input('Enter the Target'))

target_count = 0

for num in array :
    if num == target :
        target_count += 1

print(target_count)