def solve():
    line = input().split()
    n = int(line[0])
    exclude_char = line[1]
    S = input()
    
    # exclude_char의 모든 위치 찾기
    positions = [-1]  # 시작 위치
    for i in range(n):
        if S[i] == exclude_char:
            positions.append(i)
    positions.append(n)  # 끝 위치
    
    max_length = 0
    
    # 각 구간에서 가장 긴 팰린드롬 찾기
    for i in range(len(positions) - 1):
        start = positions[i] + 1
        end = positions[i + 1]
        
        if start < end:
            # 이 구간에는 exclude_char가 없음
            segment = S[start:end]
            seg_len = end - start

            input_str = "#" + "#".join(segment) + "#"
            N = len(input_str)
            A = [0 for _ in range(N)]
            
            r, p = -1, -1

            for i in range(N):
                if r < i:
                    A[i] = 0
                else:
                    ii = 2*p - i
                    A[i] = min(r-i, A[ii])
                
                while i - A[i] -1 >=0 and i+A[i] + 1 < N and input_str[i-A[i]-1] == input_str[i+A[i]+1]:
                    A[i] += 1
                if i + A[i] > r:
                    r, p = i + A[i], i
            X = max(A)
            max_length = max(max_length, X)
            
            
            # # 이 구간에서 가장 긴 팰린드롬 찾기 (중심 확장법)
            # for center in range(seg_len):
            #     # 홀수 길이
            #     l, r = center, center
            #     while l >= 0 and r < seg_len and segment[l] == segment[r]:
            #         max_length = max(max_length, r - l + 1)
            #         l -= 1
            #         r += 1
                
            #     # 짝수 길이
            #     l, r = center, center + 1
            #     while l >= 0 and r < seg_len and segment[l] == segment[r]:
            #         max_length = max(max_length, r - l + 1)
            #         l -= 1
            #         r += 1
    
    print(max_length)

solve()