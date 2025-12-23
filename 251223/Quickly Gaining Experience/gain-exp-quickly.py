n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0 for _ in range(101)] for _ in range(n)]
for idx, quest in enumerate(quests):
    e, t = quest
    dp[idx][t] = e
    for i in range(idx):
        for s in range(101):
            if dp[i][s] != 0:
                dp[idx][s+t] = max(dp[idx][s+t], dp[i][s] + e)
def cal():
    for s in range(101): 
        for i in range(n):
            if dp[i][s] >=m:
                return s
    return -1

print(cal())