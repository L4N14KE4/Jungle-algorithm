import sys
from collections import deque # 덱 쓰기 위해 import
input = sys.stdin.readline # 빠른 입력

# dfs 함수
def dfs(graph, v, visited_d):
    visited_d[v] = True # 현재 노드 방문처리
    print(v, end=" ") # 현재 노드 출력
    # 현재 노드와 연결된 다른 노드 재귀적으로 방문
    for node in sorted(graph[v]): # 정점 번호 작은순으로 정렬
        if not visited_d[node]: # 방문하지 않았다면 재귀함수 실행
            dfs(graph, node, visited_d)

# bfs 함수
def bfs(graph, start, visited_b):
    queue = deque([start]) # deque로 큐 구현
    visited_b[start] = True # 현재 노드 방문처리
    # 큐가 빌때까지
    while queue:
        v = queue.popleft() # 큐에서 하나의 노드를 뽑기
        print(v, end = " ") # 출력
        # 아직 방문하지 않은 노드를 큐에 삽입
        for node in sorted(graph[v]): # 정점 번호 작은순으로 정렬
            if not visited_b[node]: # 방문하지 않았다면
                queue.append(node) # 큐에 노드 추가
                visited_b[node] = True # 방문 처리

# 입력(노드, 간선의 갯수, 탐색 시작 노드 입력받기
n, m, start = map(int, input().rstrip().split())
# 노드가 담길 빈 리스트 생성
graph = [[] for _ in range(n + 1)]

# 간선 정보 반복문으로 입력받기
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    # 양방향 간선이므로 양쪽에 추가
    graph[a].append(b)
    graph[b].append(a)

# dfs의 방문 정보용 리스트 생성
visited_d = [False] * (n + 1)
# dfs 함수 호출
dfs(graph, start, visited_d)

print() # 줄바꿈

# bfs의 방문 정보용 리스트 생성
visited_b = [False] * (n + 1)
# bfs 함수 호출
bfs(graph, start, visited_b)