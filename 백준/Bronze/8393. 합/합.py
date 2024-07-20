import sys
sys.setrecursionlimit(1000000)

N = int(input())

def solution(num):
    if num == 1:
        return 1
    
    new_num = num - 1
    return solution(new_num) + num

print(solution(N))