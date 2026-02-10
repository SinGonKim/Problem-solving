n, k = map(int, input().split()) # k번 이동해서 최대 수집 수정 개수
string = input()


# Please write your code here.
dp = [[[0]*(k+1) for _ in range(2)] for _ in range(n)]

def initialize():
    if string[0] == 'L':
        dp[0][0][k] = 1
    else:
        dp[0][1][k] = 1

def calculation(idx, d):
    for j in range(k+1):
        dp[idx][d][j] = max(dp[idx][d][j], dp[idx-1][d][j] + 1)
        dp[idx][(d+1)%2][j] = dp[idx-1][(d+1)%2][j] 
    for j in range(k):
        dp[idx][d][j] = max(dp[idx][d][j], dp[idx-1][(d+1)%2][j+1]+1)
        
def solution():
    for i in range(1, n):
        s = string[i]
        if s == 'L':
            calculation(i, 0)
        else:
            calculation(i, 1)
    
    ans = max([max(c) for c in dp[n-1]])
    print(ans)

initialize()

solution()