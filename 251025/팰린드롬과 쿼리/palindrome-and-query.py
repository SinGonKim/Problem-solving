n, q = map(int, input().split())
S = input()
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.

dp = [[False for _  in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = True

for i in range(n-1):
    if S[i] == S[i+1]:
        dp[i][i+1] = True

for length in range(3,n+1):
    for i in range(n-length+1):
        j = i + length - 1

        if S[i] == S[j] and dp[i+1][j-1]:
            dp[i][j] = True

for a, b in queries:
    if dp[a-1][b-1]:
        print("Yes")
    else:
        print("No")
