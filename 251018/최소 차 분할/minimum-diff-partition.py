n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
s = sum(arr)

dp = [False for _ in range(s)]
dp[0] = True

for j in arr:
    for i in range(s-1,0,-1):
        if i-j < 0 or dp[i-j] == False:continue
        dp[i] = True

ans = 100_000

for i in range(1,s):
    if dp[i]:
        ans = min(ans, abs(s-i-i))
print(ans)