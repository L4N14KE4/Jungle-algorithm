n = int(input())

for _ in range(n): # 케이스 갯수만큼 반복
    nums = list(map(int, input().split())) # 학생 수, 성적 입력 받아 리스트로 저장
    avg = sum(nums[1:])/nums[0] # 평균 : 성적의 합/학생의 수 
    cnt = 0 # 평균 넘는 학생의 수
    for score in nums[1:]:
        if score > avg: # 성적이 평균을 넘으면
            cnt += 1 # 평균 넘는 학생의 수에 추가
    rate = cnt / nums[0] * 100 # 평균 넘는 학생의 백분율 구하기
    print(f"{rate:.3f}%") # 소수점 3번째 자리까지 출력