n = int(input())

# Please write your code here.
memo = [0 for _ in range(n+1)]
memo[2] = 1
if n >=3:
    memo[3] = 1

for i in range(4,n+1):
    memo[i] = (memo[i-2] + memo[i-3])%10007

ans = memo[n]
print(ans)