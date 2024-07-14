values = [input() for _ in range(3)] # 3개의 숫자 입력받기

result_num = int(values[0]) + int(values[1]) - int(values[2]) # 숫자로 계산
result_str = int(values[0] + values[1]) - int(values[2]) # 문자열로 계산

# 출력
print(result_num)
print(result_str)