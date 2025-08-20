n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dp = [0 for _ in range(n)]
dp[0] = jobs[0][2]

for i in range(1,n):
    for j in range(i):
        if jobs[j][1] < jobs[i][0]:
            dp[i] = max(dp[i], dp[j] + jobs[i][2])
        else:
            dp[i] = max(dp[i], jobs[i][2])
print(max(dp))