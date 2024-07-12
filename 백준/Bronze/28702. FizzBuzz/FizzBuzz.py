# 마지막 입력부터 처리하기 위해 3, 2, 1 순서로 3번 반복
for i in range(3, 0, -1):
    x = input()
    # 입력이 숫자라면
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
        # 숫자 정수형으로 변환 + i를 더해 다음 문자열 계산
        n = int(x) + i

if n % 3 ==0 and n % 5 == 0:
    print('FizzBuzz')
elif n %3 == 0:
    print('Fizz')
elif n %5 == 0:
    print('Buzz')
else:
    print(n)