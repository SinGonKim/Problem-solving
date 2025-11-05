
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
def solve():
    # 입력 받기
    n, m, k = map(int, input().split())
    
    # 그래프 구성 (인접 리스트)
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    order = list(map(int, input().split()))
    
    visited = [0 for _ in range(n+1)]
    answer = 0
    def dfs(x,idx):
        nonlocal answer
        if idx == k:
            answer = 1
            return
        visited[x] = 1
        for nx in graph[x]:
            if visited[nx]:continue
            elif visited[nx] == 0 and nx == order[idx]:
                # print(x, nx, idx)
                dfs(nx, idx+1)
                visited[nx] = 0
            else:
                # print(x, nx, idx)
                dfs(nx, idx)
                visited[nx] = 0
        return
    dfs(order[0],1)
    print(answer)

if __name__ == "__main__":
    solve()