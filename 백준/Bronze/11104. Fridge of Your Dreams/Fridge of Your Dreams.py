import sys

input = sys.stdin.readline
def binary_to_decimal(bin):
    decimal = 0
    power = 0

    for bit in bin[::-1]:
        if bit == '1':
            decimal += 2 ** power
        power += 1

    return decimal

N = int(input().strip())
for bins in range(N):
    bin = input().strip()
    result = binary_to_decimal(bin)
    print(result)