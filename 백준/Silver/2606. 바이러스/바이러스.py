import sys
from collections import deque

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

# N+1 크기의 리스트를 만들고, 각 요소를 빈 리스트로 초기화
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    # 양방향 그래프이므로 양쪽 모두에 추가
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    cnt = 0
    
    while queue:
        visit = queue.popleft()
        cnt += 1
        for computer in graph[visit]:
            if not visited[computer]:
                queue.append(computer)
                visited[computer] = True
    # 1번 컴퓨터 제외
    return cnt - 1

result = bfs(graph, 1)
print(result)