n, k = map(int, input().split()) # k번 이동해서 최대 수집 수정 개수
string = 'L' + input()


# Please write your code here.
dp = [[[0]*(k+1) for _ in range(2)] for _ in range(n+1)]

def initialize():
    dp[0][0][k] = 1

def calculation(cnt):
    dir_map = {'L': 0, 'R': 1}
    for idx in range(1,n+1):
        s = string[idx]
        d = dir_map[s]

        # 움직이지 않을 시
        if dp[idx-1][d][cnt] != 0:
            dp[idx][d][cnt] = max(dp[idx][d][cnt], dp[idx-1][d][cnt] + 1)
        dp[idx][(d+1)%2][cnt] = dp[idx-1][(d+1)%2][cnt]
        
        # 움직일 기회가 있고 움직일 때
        if cnt >= 1:
            dp[idx][d][cnt-1] = max(dp[idx][d][cnt-1], dp[idx-1][(d+1)%2][cnt]+1)
         
        
def solution():
    for num in range(k, -1, -1):
        calculation(num)
    
    ans = max([max(c) for c in dp[n-1]])
    print(ans)


initialize()

solution()