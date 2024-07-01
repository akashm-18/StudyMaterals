def find_all_subarrays(nums):
    subarrays = []
    n = len(nums)
    # Include individual elements
    for i in range(n):
        subarrays.append([nums[i]])
    
    # Include all contiguous subarrays
    for i in range(n):
        for j in range(i + 1, n + 1):
            subarrays.append(nums[i:j])
    
    # Include subarrays with skips
    for i in range(n):
        for j in range(i + 2, n + 1):
            subarrays.append(nums[i:j])
    
    return subarrays

array = []
while True:
    try:
        value = input("Enter the number (type 'done' to stop): ")
        if value.lower() == "done":
            break
        else:
            array.append(int(value))
    except ValueError:
        print("Enter a valid number")

subarrays = find_all_subarrays(array)
for subarray in subarrays:
    print(subarray)
