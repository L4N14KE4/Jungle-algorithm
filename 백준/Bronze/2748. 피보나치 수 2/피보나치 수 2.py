# dp - bottom up(상향식) - 반복문
n = int(input())

if n <= 1: # 입력한 숫자가 1 이하라면
    print(n) # 그대로 출력
    
else: # n = 2 이상인 경우만
    fibo = [0] * (n + 1) # 입력 숫자 + 1개의 요소 생성
    fibo[1] = 1 # 피보나치 수열 1은 1로 지정
    for num in range(2, n + 1): # 2부터 목표 숫자까지 순회하며
        fibo[num] = fibo[num - 1] + fibo[num - 2] # 피보나치 함수 점화식대로 계산
    
    print(fibo[n]) # 출력