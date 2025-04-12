
N = int(input())
memo = [-1 for _ in range(N+1)]
memo[1] = 1
if N>=2:
    memo[2] = 1
# Please write your code here.
def solve(n):
    if n == 1 or n==2:
        return 1
    elif memo[n] != -1:
        return memo[n]
    else:
        memo[n] = solve(n-1) + solve(n-2)
        return memo[n]

ans = solve(N) 
print(ans)