n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(n-1,-1,-1):
    ans += k//coins[i]
    k %= coins[i]
print(ans)
    