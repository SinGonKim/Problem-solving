import sys
input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    T =list(map(int, input().split()))
    dp = [[0 for _ in range(n)]for _ in range(n)]
    for num_len in range(n): #for문을 시작점 끝점으로 잡으면 문제가 생김 뒤에 dp[start+1][end] 에서 dp[start]정산 과정에 dp[start+1]이 정산 전에 나오게 되므로 계산이 정확히 되지 않음
        for start in range(n-num_len):
            end = num_len+start #끝점
            if start==end:
                dp[start][end] = 1
            elif T[start] == T[end]:
                if start+1 == end:
                    dp[start][end] = 1
                elif dp[start+1][end-1] == 1: 
                    dp[start][end] =1
    for _ in range(int(input())):
        s, e = map(int, input().split())
        print(dp[s-1][e-1])
