import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def bellman_ford(start):
    dp[start] = 0

    # n번의 라운드를 반복
    for i in range(1, n+1):
        # 매 라운드마다 모든 간선을 확인
        for j in range(m):
            now, next, cost = graph[j][0], graph[j][1], graph[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dp[now] != INF and dp[next] > dp[now] + cost:
                dp[next] = dp[now] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환 존재
                if i == n:
                    return True
    return False
if __name__=="__main__":
    n, m = map(int, input().split())
    graph = []
    for _ in range(m):
        a, b, c = map(int,input().split())
        graph.append((a,b,c))
    dp = [INF for _ in range(n+1)]
    negative_cycle = bellman_ford(1)

    if negative_cycle:
        print(-1)
    else:
        for i in range(2,n+1):
            if dp[i] == INF:
                print(-1)
            else:
                print(dp[i])
