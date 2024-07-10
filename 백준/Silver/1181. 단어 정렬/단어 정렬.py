# 리스트를 활용한 풀이
words = []
N = int(input())

for _ in range(N):
    word = input() # 단어들 입력받기
    if word not in words: # 중복 확인
        words.append(word) # 중복 없으면 리스트에 추가

# 람다함수로 단어의 길이와 단어를 튜플로 만들고,
# sort 함수로 튜플로 만든 비교키로 비교 및 정렬
words.sort(key=lambda x:(len(x), x))

for word in words: # 한줄에 단어 하나씩 출력
    print(word)