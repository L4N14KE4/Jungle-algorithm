# 세트를 이용한 풀이
words = set() 
N = int(input())

for _ in range(N):
    word = input().strip() 
    # strip 함수는 여기서는 필요 없음 -> 그냥 씀
    words.add(word)

# 세트를 리스트로 만들어 리스트와 동일하게 람다 함수를 이용해 튜플로 만듦.
# sorted 함수로 튜플로 만든 비교키로 비교 및 정렬 후 sorted_words라는 새 리스트에 저장
sorted_words = sorted(list(words), key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)