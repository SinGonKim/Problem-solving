n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# dp[mask]: mask(비트)에 해당하는 열들을 이미 채웠을 때의 최대값
dp = [-1] * (1 << n)
dp[0] = 0

for mask in range(1 << n):
    if dp[mask] == -1: continue
    
    # 다음에 채울 행의 번호는 현재 mask에서 1이 된 비트의 개수와 같음
    r = bin(mask).count('1')
    if r == n: break
    
    for c in range(n):
        # c번째 열을 아직 사용하지 않았다면
        if not (mask & (1 << c)):
            next_mask = mask | (1 << c)
            dp[next_mask] = max(dp[next_mask], dp[mask] + grid[r][c])

print(dp[(1 << n) - 1])