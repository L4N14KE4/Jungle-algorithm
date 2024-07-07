h, m = map(int, input().split())
if m < 45:
    if h == 0: h = 23
    else: h -= 1
    m = 60 - (45 - m)
else: m -= 45
    
print(h, m)