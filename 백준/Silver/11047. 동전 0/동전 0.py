N, K = map(int, input().split())

def coinCounter(coin_num, change):
    cnt = 0
    coins = []
    for i in range(coin_num):
        coins.append(int(input()))
    for coin in reversed(coins):
        if coin > change:
            continue
        cnt += change // coin
        change = change % coin
    return cnt

result = coinCounter(N, K)
print(result)