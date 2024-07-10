N, M = map(int, input().split())
cards = list(map(int, input().split()))

my_max = 0

for first in range(N - 2):
    for second in range(first + 1, N - 1):
        for third in range(second + 1, N):
            my_sum = cards[first] + cards[second] + cards[third]
            if my_max < my_sum <= M:
                my_max = my_sum
                
print(my_max)