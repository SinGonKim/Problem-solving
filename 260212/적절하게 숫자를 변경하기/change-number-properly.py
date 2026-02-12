N, M = map(int, input().split()) # 길이, 인접한 두 숫자가 다른 횟수 M
a = [0] + list(map(int, input().split()))

# Please write your code here.
# 유사도가 높게

dp = [[[-1, -1, -1, -1] for _ in range(M+1)] for _ in range(N+1)]

def initilize():
    for num in range(4):
        if num == a[1] - 1:
            dp[1][M][num] = 1
        else:
            dp[1][M][num] = 0

initilize()

for i in range(2,N+1): # O(500*100*4*4*2)
    cur_str = a[i] - 1
    for m in range(M, -1, -1):
        for prev_num in range(4):
            if dp[i-1][m][prev_num] == -1: continue
            # CASE
            for cur_num in range(4):
                score = 1 if cur_str == cur_num else 0
                if cur_num == prev_num: # 인접한 두 숫자가 같음
                    dp[i][m][cur_num] = max(dp[i][m][cur_num], dp[i-1][m][prev_num] + score)
                elif m > 0: # 인접한 두 숫자가 다름. 숫자가 바뀜
                    dp[i][m-1][cur_num] = max(dp[i][m-1][cur_num], dp[i-1][m][prev_num] + score)

ans = 0
for m in range(M+1):
    for num in range(4):
        if ans < dp[N][m][num]:
            ans = dp[N][m][num]
print(ans)
