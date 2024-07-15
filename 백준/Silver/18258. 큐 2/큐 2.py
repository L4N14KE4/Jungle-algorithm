import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque([])
for i in range(N):
    insts = sys.stdin.readline().strip().split()
    
    inst = insts[0]
    
    if inst == "push":
        queue.append(insts[1])
    elif inst == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif inst == "size":
        print(len(queue))
    elif inst == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif inst == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif inst == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])