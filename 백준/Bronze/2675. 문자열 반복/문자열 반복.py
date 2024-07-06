case = int(input())
for _ in range(case):
    result = ""
    R, S = map(str, input().split())
    for i in range(len(S)):
        result += S[i] * int(R)
    print(result)