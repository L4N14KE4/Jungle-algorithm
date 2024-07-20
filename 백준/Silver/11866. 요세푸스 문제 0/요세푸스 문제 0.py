import sys
from collections import deque

# N명 # 제거할 순서
N, K = map(int, input().split())

people = deque() # 큐 구현 위해 deque 만들기
josephus = [] # 재거할 순서 담을 리스트

for p in range(1 , N + 1): # N명만큼 people에 순서대로 더하기
    people.append(p)
    
while len(people) > 0: # people 큐에 사랑이 낭아있는 동안
    for j in range(1, K): # K - 1번 반복
        people.append(people.popleft()) # 맨앖에 있는 사람을 제거하고, 다시 append로 큐의 맨뒤에 추가
        # 회전하는 효과가 있음

    josephus.append(str(people.popleft())) # K번째 사람이 큐의 맨 앞에 있게됨. 큐에서 제거하고 요새푸스 리스트에 추가

print("<{}>".format(', '.join(josephus))) # 포맷에 맞춰서 요새푸스 순열 출력

    