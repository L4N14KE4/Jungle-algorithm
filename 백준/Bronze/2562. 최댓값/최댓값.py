import sys

# 자연수 저장 리스트
numbers = []

# 9개 자연수 입력받기
for _ in range(9):
  numbers.append(int(sys.stdin.readline()))
  # 입력받은 값을 리스트에 추가

max_value = max(numbers)
max_index = numbers.index(max_value) + 1
# n번째에 있는지 물었으므로, index + 1
  
print(max_value)
print(max_index)