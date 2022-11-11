import sys
input = sys.stdin.readline
n, m = map(int, input().split())
M = [0] + list(map(int,input().split()))
C = [0] + list(map(int,input().split()))
dp = [[0 for _ in range(sum(C)+1)]for _ in range(n+1)]
result = sum(C)

for i in range(1,n+1): #메모리 한바퀴 돌거다.
    memory = M[i]
    cost = C[i]
    for j in range(1, sum(C)+1):
        if j< cost: #현재 앱을 비활성화시킬만큼의 cost가 충분하지 않은 경우
            dp[i][j] = dp[i-1][j]
        else: #같은 cost내에서 현재 앱을 끈 뒤의 메모리와 현재 앱을 끄지 않았을 때 메모리를 비교
            dp[i][j] = max(memory+dp[i-1][j-cost], dp[i-1][j])
        if dp[i][j] >= m: #조건이 충족된다면
            result = min(result,j) # 더 작은 cost 값으로 갱신
if m != 0:
    print(result)
else:
    print(0)
