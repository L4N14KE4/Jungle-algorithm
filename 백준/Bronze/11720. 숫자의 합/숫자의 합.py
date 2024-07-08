n = int(input())
num = list(input()) # 숫자 리스트로 입력ㅈ
result = 0 # 결과 변수 초기화
for i in range(n): # 단어 길이만큼 반복ㄷ
    result += int(num[i]) # 정수 형태로 변환 후 덧셈
print(result)