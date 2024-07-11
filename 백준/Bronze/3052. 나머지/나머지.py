# 리스트 풀이
arr = [] # 고유값 넣을 리스트 생성
for i in range(10):
    a = int(input())
    if a % 42 not in arr: # 42로 나눈 나머지가 리스트에 없다면
        arr.append(a % 42) # 리스트에 추가

print(len(arr)) # 고유값 갯수 출력

# # set 풀이
# arr = [] # 고유값 넣을 리스트 생성
# for i in range(10):
#     a = int(input())
#     arr.append(a % 42)

# print(len(set(arr))) # 고유값 갯수 출력