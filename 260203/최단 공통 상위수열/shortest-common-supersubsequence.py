import sys
sys.setrecursionlimit(10*8)
s = input()
t = input()

n = len(s)
m = len(t)

# dp[i][j]는 s의 i번째, t의 j번째까지 고려했을 때의 최단 공통 상위수열의 길이
dp = [[0] * (m + 1) for _ in range(n + 1)]

# 초기 조건 설정
for i in range(n + 1):
    dp[i][0] = i  # t가 빈 문자열이면 s의 모든 문자를 추가해야 함
for j in range(m + 1):
    dp[0][j] = j  # s가 빈 문자열이면 t의 모든 문자를 추가해야 함

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s[i-1] == t[j-1]:
            # 두 문자가 같으면 공통으로 한 번만 카운트하고 대각선에서 +1
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            # 다르면 s에서 하나를 가져오거나 t에서 하나를 가져오는 것 중 최소값 + 1
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

print(dp[n][m])