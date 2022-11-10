import sys
input = sys.stdin.readline
n, k = map(int, input().split())
menu = [] # 코인 종류
for _ in range(n):
    menu.append(int(input()))
dp = [0 for _ in range(k+1)] # 사이즈 k+1만큼의 리스트 선언
dp[0] = 1 # 동전 한 개만 쓸 때의 경우의 수 고려하기 위해 선언

for i in menu:
    for j in range(i,k+1):
        if j-i >=0:
            dp[j] += dp[j-i]
print(dp[k])
