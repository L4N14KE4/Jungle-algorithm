# 라이브러리 불러오기
from collections import deque
import sys
input = sys.stdin.readline

# bfs 함수
# graph: 그래프 인접 리스트
# start: 탐색 시작할 노드
# visited: 노드 방문 여부 저장 리스트
def bfs(graph, start, visited):
    queue = deque([start]) # 시작 노드 큐에 삽입
    visited[start] = True # 시작 노드 방문처리
    
    while queue: # 큐 빌때까지 반복
        v = queue.popleft() # 큐에서 하나의 노드를 뽑기
        for i in graph[v]: # 근접 노드
            if not visited[i]: # 방문하지 않았다면
                queue.append(i) # 큐에 노드 추가
                visited[i] = True # 방문 처리

# 입력
N, M = map(int, input().rstrip().split()) # 노드의 개수, 연결 요소의 개수 입력받기
graph = [[] for _ in range(N + 1)] # 그래프 초기화
visited = [False] * (N + 1) # 방문여부 저장할 리스트 추가

# 그래프 구성
for _ in range(M): # 
    node1, node2 = map(int, input().split()) # 간선의 양 끝점 = 근접 노드
    graph[node2].append(node1) # 무방향 그래프 양쪽으로 간선 추가
    graph[node1].append(node2)
    
cnt = 0 # 연결 요소 개수 저장할 변수

# 모든 노드에 대해 BFS 수행
for i in range(1, N + 1): # 1부터 N까지의 모든 노드에서
    if not visited[i]: # 방문하지 않은 노드라면
        bfs(graph, i, visited) # BFS 실행
        cnt += 1 # 연결 요수 개수 증가

print(cnt) # 연결 요소 총 개수 출력