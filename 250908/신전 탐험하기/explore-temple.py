n = int(input())
l, m, r = [], [], []
for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)

# Please write your code here.
dp = [[0,0,0] for _ in range(n)]
dp[0][0] = l[0]
dp[0][1] = m[0]
dp[0][2] = r[0]
for i in range(1,n):
    dp[i][0] = max(dp[i-1][1]+l[i], dp[i-1][2]+l[i], dp[i][0])
    dp[i][1] = max(dp[i-1][0]+m[i], dp[i-1][2]+m[i], dp[i][1])
    dp[i][2] = max(dp[i-1][0]+r[i], dp[i-1][1]+r[i], dp[i][2])
print(max(dp[n-1]))