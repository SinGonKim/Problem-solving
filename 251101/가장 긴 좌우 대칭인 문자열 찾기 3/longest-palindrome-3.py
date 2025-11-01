def manacher(s):
    # '#'을 삽입하여 홀수 길이로 변환
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C = R = 0
    
    for i in range(1, n-1):
        # 미러 인덱스
        i_mirror = 2*C - i
        
        if R > i:
            P[i] = min(R - i, P[i_mirror])
        
        # 중심에서 확장
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1
        
        # 경계 업데이트
        if i + P[i] > R:
            C, R = i, i + P[i]
    
    return P

def solve():
    line = input().split()
    n = int(line[0])
    exclude_char = line[1]
    S = input()
    
    # Manacher로 모든 팰린드롬 길이 구하기
    P = manacher(S)
    T = '#'.join('^{}$'.format(S))
    
    max_length = 0
    
    for i in range(2, len(T)-2):
        # 팰린드롬 길이
        length = P[i]
        center_in_S = (i - 2) // 2
        
        # 원본 문자열에서 팰린드롬 범위 계산
        if i % 2 == 0:  # '#' 위치 (짝수 길이 팰린드롬)
            left = center_in_S - length // 2 + 1
            right = center_in_S + length // 2
        else:  # 문자 위치 (홀수 길이 팰린드롬)
            left = center_in_S - length // 2
            right = center_in_S + length // 2
        
        # 각 가능한 팰린드롬 길이에 대해 체크
        for l in range(length, -1, -1):
            if i % 2 == 0:
                actual_left = center_in_S - l // 2 + 1
                actual_right = center_in_S + l // 2
            else:
                actual_left = center_in_S - l // 2
                actual_right = center_in_S + l // 2
            
            if actual_left >= 0 and actual_right < n:
                substring = S[actual_left:actual_right+1]
                if exclude_char not in substring:
                    max_length = max(max_length, len(substring))
    
    print(max_length)