a, b, c = map(int, input().split())
# 연쇄 비교(Chained Comparison) - 파이썬만 지원
if a == b == c:
    print(10000 + a * 1000)

# 연쇄 비교 사용하지 않고 구현
# if a == b & b == c:
#     print(10000 + a * 1000)

elif a == b or a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max(a, b, c) * 100)