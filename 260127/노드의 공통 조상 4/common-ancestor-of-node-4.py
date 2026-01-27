import sys

# 재귀 깊이 제한 해제 (DFS 사용 시 필수)
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def solve():
    # 1. 입력 받기
    n = int(input())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # 2. 깊이(depth)와 부모(parent) 배열 초기화
    depth = [-1] * (n + 1)
    parent = [0] * (n + 1)

    # 3. DFS를 통해 각 노드의 깊이와 부모 설정
    def dfs(curr, d):
        depth[curr] = d
        for neighbor in adj[curr]:
            if depth[neighbor] == -1: # 방문하지 않은 노드라면
                parent[neighbor] = curr
                dfs(neighbor, d + 1)

    # 루트는 1번 노드
    dfs(1, 0)

    # 4. LCA 함수 정의
    def get_lca(u, v):
        # 깊이 맞추기 (u가 더 깊게 설정)
        if depth[u] < depth[v]:
            u, v = v, u
        
        while depth[u] > depth[v]:
            u = parent[u]
        
        # 두 노드가 같아질 때까지 위로 이동
        while u != v:
            u = parent[u]
            v = parent[v]
        
        return u

    # 5. 쿼리 처리
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        print(get_lca(u, v))

solve()