import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
a = input()
b = input()

# Please write your code here.
dp = [[INF]*10 for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(10):
        if dp[i][j] == INF: continue
    
        ai = ord(a[i]) - ord('0')
        bi = ord(b[i]) - ord('0')

        cur = (j + ai) % 10
        new_ccw = (bi - cur) % 10
        new_cw = (10 - new_ccw) % 10

        nj = (j + new_ccw)%10
        dp[i+1][nj] = min(dp[i+1][nj], dp[i][j] + new_ccw)

        dp[i+1][j] = min(dp[i+1][j], dp[i][j] + new_cw)
print(min(dp[N]))