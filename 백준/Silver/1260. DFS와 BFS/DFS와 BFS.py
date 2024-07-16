import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, v, visited_d):
    visited_d[v] = True
    print(v, end=" ")
    for node in sorted(graph[v]):
        if not visited_d[node]:
            dfs(graph, node, visited_d)
            
def bfs(graph, start, visited_b):
    queue = deque([start])
    visited_b[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for node in sorted(graph[v]):
            if not visited_b[node]:
                queue.append(node)
                visited_b[node] = True

n, m, start = map(int, input().rstrip().split())
graph = [[] for j in range(n + 1)]
for k in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited_d = [False] * (n + 1)
dfs(graph, start, visited_d)

print()

visited_b = [False] * (n + 1)
bfs(graph, start, visited_b)