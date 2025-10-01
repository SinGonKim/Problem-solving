n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
prefix_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + arr[i-1][j-1]


 
max_sum = -1

# 모든 가능한 K x K 정사각형 탐색
for i in range(k, n + 1):
    for j in range(k, n + 1):
        current_sum = (prefix_sum[i][j] - 
                        prefix_sum[i-k][j] - 
                        prefix_sum[i][j-k] + 
                        prefix_sum[i-k][j-k])
        
        # 최댓값 갱신
        if current_sum > max_sum:
            max_sum = current_sum

# 결과 출력
print(max_sum)
