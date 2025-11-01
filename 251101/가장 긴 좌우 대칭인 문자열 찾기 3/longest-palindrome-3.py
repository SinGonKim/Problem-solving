def solve():
    line = input().split()
    n = int(line[0])
    exclude_char = line[1]
    S = input()
    
    max_length = 0
    
    # 중심 확장법 사용 - O(n²)
    for center in range(n):
        # 홀수 길이 팰린드롬
        l, r = center, center
        while l >= 0 and r < n and S[l] == S[r]:
            # exclude_char를 포함하지 않는 경우만
            if exclude_char not in S[l:r+1]:
                max_length = max(max_length, r - l + 1)
            l -= 1
            r += 1
        
        # 짝수 길이 팰린드롬
        l, r = center, center + 1
        while l >= 0 and r < n and S[l] == S[r]:
            # exclude_char를 포함하지 않는 경우만
            if exclude_char not in S[l:r+1]:
                max_length = max(max_length, r - l + 1)
            l -= 1
            r += 1
    
    print(max_length)

solve()