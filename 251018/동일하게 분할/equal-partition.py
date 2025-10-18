n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
s = sum(arr)
dp = [0 for _ in range(s+1)]

dp[0] = 1

for j in arr:
    for i in range(s,0,-1):
        if i-j >=0 and dp[i-j]:
            dp[i] = 1

if s%2 or dp[s//2] == 0:
    print('No')
else:
    print('Yes')