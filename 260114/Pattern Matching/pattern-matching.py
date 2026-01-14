import sys

# 입력 받기
s = input().strip()
p = input().strip()

n, m = len(s), len(p)

# dp[i][j]는 s[i:]와 p[j:]가 매칭되는지 여부를 저장
dp = [[False] * (m + 1) for _ in range(n + 1)]

# 베이스 케이스: 빈 문자열과 빈 패턴은 일치함
dp[n][m] = True

for i in range(n, -1, -1):
    for j in range(m-1, -1, -1):
        first_match = (i<n) and (s[i] == p[j] or p[j] == '.')

        if j + 1 < m and p[j+1] == '*':
            dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
        else:
            dp[i][j] = first_match and dp[i+1][j+1]

# 결과 출력
if dp[0][0]:
    print("true")
else:
    print("false")