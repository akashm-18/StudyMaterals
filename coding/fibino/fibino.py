n = int(input("Enter the number of terms"))
first = 0
second = 1

for i in range(n):
    print(first)
    tempFirst = first
    first = second
    second = second + tempFirst
    