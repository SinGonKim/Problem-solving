n = int(input())

# Please write your code here.
memo = [0 for _ in range(n+1)]
memo[2] = 1
if n >=3:
    memo[3] = 1

def solve(x):
    if memo[x] != 0:
        return memo[x]
    elif x >= 3:
        memo[x] = memo[x-2] + memo[x-3]
        return memo[x]
    elif x>=2:
        memo[x] = memo[x-2]
        return memo[x]

ans = solve(n)
print(ans)