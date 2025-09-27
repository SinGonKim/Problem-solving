n = int(input())

A = []
for _ in range(n):
    left, mid, right = map(int, input().split())
    A.append((left,mid,right))

# Please write your code here.
dp = [[[0]*3 for _ in range(3)] for _ in range(n+1)]

for idx, a in enumerate(A,1):
    for i in range(3):
        if idx == 1:
            dp[idx][i][i] = a[i]
            continue
        for j in range(3):
            dp[idx][i][j] = max(dp[idx-1][(i+1)%3][j] + a[i], dp[idx-1][(i+2)%3][j]+a[i])

answer = 0
for i in range(3):
    for j in range(3):
        if i == j: continue
        answer = max(answer, dp[n][i][j])

print(answer)
