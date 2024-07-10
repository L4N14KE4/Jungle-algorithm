import sys
input = sys.stdin.readline
n = int(input().rstrip())
all_score = [] # 학생의 수

for _ in range(n):
    score = list(input().rstrip().split())
    all_score.append((score[0], int(score[1]), int(score[2]), int(score[3])))
    
all_score.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in all_score:
    print(i[0])