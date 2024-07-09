heights = [] # 키 받을 리스트
# 9명 입력받고 리스트에 저장
for _ in range(9):
    height = int(input())
    heights.append(height)
    
total = 0 # 키들의 합
for height in heights:
    total += height

# (0,1) 부터 (7, 8)까지의 모든 경우의 수 생성
for i in range(8): # 1~7
    for j in range(i + 1, 9): # 1~8
        # 전체 키에서 두명의 키를 뺐을때 100이면 나머지가 진짜 난쟁이
        if total - heights[i] - heights[j] == 100:
            real_dwarfs = [] # 진짜 난쟁이 담을 리스트
            for h in heights: 
                # 키 리스트에서 가짜 난쟁이 제외하고 진짜 난쟁이 리스트에 저장
                if h != heights[i] and h!= heights[j]:
                    real_dwarfs.append(h)

            # 키순서대로 정렬하기
            real_dwarfs.sort()
            
            # 출력
            for dwarf in real_dwarfs:
                print(dwarf)
            
            exit()