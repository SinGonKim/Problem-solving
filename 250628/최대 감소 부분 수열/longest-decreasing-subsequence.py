import sys

n = int(input())
arr = list(map(int, input().split()))

min_val = -sys.maxsize 
dp = [min_val  for _ in range(n)]
dp[0] = 0

for i in range(1, n) : 
    for j in range(i) : 
        
        if arr[i] < arr[j] : 
            #print(arr[i], arr[j])
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp) + 1)
