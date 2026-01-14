import sys

# 입력 받기
s = input().strip()
p = input().strip()

n, m = len(s), len(p)
dp = [[False] * (m + 1) for _ in range(n + 2)]
s = " " + s
p = " " + p

dp[0][0] = True

for j in range(m):
    for i in range(n+1):
        if not dp[i][j]: continue

        if j != m - 1 and p[j+2] == "*":
            dp[i][j+2] = True

            for curi in range(i+1,n+1):
                if p[j+1] != '.' and s[curi] != p[j+1]:break
                dp[curi][j+2] = True
        elif p[j+1] == '.':
            dp[i+1][j+1] = True
        else:
            if i != n and s[i+1] == p[j+1]:
                dp[i+1][j+1] = True
print('true' if dp[n][m] else 'false')