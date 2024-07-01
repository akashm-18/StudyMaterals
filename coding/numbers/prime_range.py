def check_prime(number):
    if number <= 1 :
        return False
    for i in range(2,int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def find_the_range(start,end):
    primes = []
    for i in range(start,end + 1):
        if check_prime(i):
            primes.append(i)
    return primes



start_range = int(input('Enter the start Range : '))
end_range = int(input('Enter the End Range : '))

result = find_the_range(start_range,end_range)
print('Prime Numbers are : ',result)