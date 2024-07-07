def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
        
def countPrimes(numbers):
    count = 0
    for num in numbers:
        if isPrime(num):
            count += 1
    return count

N = int(input())
numbers = list(map(int, input().split()))
    
result = countPrimes(numbers)
print(result)