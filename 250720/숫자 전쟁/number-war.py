n = int(input())
first_cards = [0] + list(map(int, input().split()))
second_cards = [0] + list(map(int, input().split()))

# Please write your code here.

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, len(first_cards)):
    for j in range(1, len(second_cards)):
        if first_cards[i] < second_cards[j]:
            dp[i][j] = max(dp[i-1][j-1], dp[i][j])
            dp[i][j] = max(dp[i-1][j], dp[i][j])
        else:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + second_cards[j])
print(dp[n][n])