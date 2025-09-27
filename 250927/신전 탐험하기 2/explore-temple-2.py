n = int(input())

A = []
for _ in range(n):
    left, mid, right = map(int, input().split())
    A.append((left,mid,right))

# Please write your code here.
dp = [[0 for _ in range(3)] for _ in range(n+1)]

for idx, a in enumerate(A,1):
    for i in range(3):
        dp[idx][i] = max(dp[idx-1][(i+1)%3] + a[i], dp[idx-1][(i+2)%3]+a[i])
print(max(dp[n]))
