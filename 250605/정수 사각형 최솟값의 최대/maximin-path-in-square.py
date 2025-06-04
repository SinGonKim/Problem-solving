def max_min_path():
    # dp[i][j]: (i,j)까지 오는 경로에서 거친 숫자들 중 최소값의 최대값
    dp = [[0] * N for _ in range(N)]
    
    # 시작점
    dp[0][0] = grid[0][0]

    # 첫 번째 행
    for j in range(1, N):
        dp[0][j] = min(dp[0][j - 1], grid[0][j])

    # 첫 번째 열
    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][0], grid[i][0])

    # 나머지 셀
    for i in range(1, N):
        for j in range(1, N):
            from_top = min(dp[i - 1][j], grid[i][j])
            from_left = min(dp[i][j - 1], grid[i][j])
            dp[i][j] = max(from_top, from_left)

    return dp[N - 1][N - 1]


# Please write your code here.
if __name__ == "__main__":
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    ans = max_min_path()
    print(ans)
