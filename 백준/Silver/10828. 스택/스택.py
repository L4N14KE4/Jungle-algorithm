import sys
N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    x = sys.stdin.readline().rstrip()

    if "push" in x:
        p, num = x.split()
        stack.append(int(num))

    elif "pop" in x:
        if len(stack) == 0:
            print(-1)
        else: print(stack.pop()) 
            
    elif "size" in x:
        print(len(stack))
        
    elif "empty" in x:
        if len(stack) == 0:
            print(1)
        else: print(0)
            
    elif "top" in x:
        if len(stack) == 0:
            print(-1)
        else: print(stack[-1])
