n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
new_sequence = sequence[::-1]

up_dp = [1 for _ in range(n)]
down_dp = [1 for _ in range(n)]

for i in range(1,n):
    for j in range(i):
        if sequence[i] > sequence[j]:
            up_dp[i] = max(up_dp[j]+1, up_dp[i])

for i in range(1,n):
    for j in range(i):
        if new_sequence[j] < new_sequence[i]:
            down_dp[i] = max(down_dp[j]+1, down_dp[i])

result = 0
for i in range(n):
    maxi = up_dp[i] + down_dp[n-i-1] - 1
    result = max(maxi, result)
print(result)