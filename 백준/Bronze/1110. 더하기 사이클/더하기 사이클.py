N = int(input())
num = N # 원래 숫자 길이
cycle = 0 # 사이클 지정

while True:
    # 10으로 나눠 몫과 나머지 구하기
    # 십의 자리 / 일의 자리
    a = num // 10 # 몫
    b = num % 10 # 나머지
    c = (a + b) % 10 # 두 수를 더했을때의 나머지
    num = (b * 10) + c # 나머지(b)를 10의 자리로, c를 1의 자리로
    cycle += 1
    if num == N:
        break

print(cycle)