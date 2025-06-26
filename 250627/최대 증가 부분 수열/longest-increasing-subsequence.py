n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
import bisect
dp = [1 for _ in range(n)]
stack = []
stack.append(m[0])

for i in range(1,n):
    idx = bisect.bisect_left(stack,m[i])
    if idx == len(stack):
        stack.append(m[i])
        dp[i] = dp[idx-1]+1
    else:
        stack[idx] = m[i]
        dp[i] = dp[idx]
 
print(max(dp))

