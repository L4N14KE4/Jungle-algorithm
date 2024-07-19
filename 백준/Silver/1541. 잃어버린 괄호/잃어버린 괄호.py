# exp -> expression
exp = input().split('-') # # 식을 입력받고 - 기준으로 split
result = 0 # 최솟값 담을 변수 선언
for num in exp[0].split('+'): # 리스트의 첫번째 인덱스에 대해 + 연산
    # 연산 결과를 최솟값에 추가 
    result += int(num)
    # subtraction -> sub
for sub in exp[1:]: # 두번째 인덱스부터
    for num in sub.split('+'): # + 기준으로 split
        result -= int(num) # 연산결과에서 숫자 빼기

print(result)