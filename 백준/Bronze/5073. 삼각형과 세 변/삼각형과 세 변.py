while True: 
    a, b, c = map(int, input().split())
    # 탈출 조건
    if a == b == c == 0:
        break
    
    # 삼각형 조건 체크용 - 큰수대로 정렬
    num = sorted([a, b, c], reverse=True)
    
    # 두 변의 길이의 합이 나머지 한변의 길이보다 커야함
    # 조건 달성하지 못한 경우
    if num[0] >= num[1] + num[2]:
        print("Invalid")
        
    # 세 변의 길이가 모두 같은 경우
    elif a == b == c:
        print("Equilateral")
        
    # 두 변의 길이만 같은 경우
    elif a == b or a == c or b == c:
        print("Isosceles")
    # elif a == b != c or a == c != b or b == c != a:
    #     print("Isosceles")
    
    # 세 변의 길이가 모두 다른 경우
    else:
        print("Scalene")