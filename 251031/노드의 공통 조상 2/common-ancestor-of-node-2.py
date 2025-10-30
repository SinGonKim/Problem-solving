import sys

# 재귀 깊이 제한을 늘려줍니다 (깊은 트리의 DFS를 위함)
sys.setrecursionlimit(10**6)
# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

N = int(input())

# N의 최대 크기가 50,000이므로, log2(50000)은 약 15.6입니다.
# 2^16 = 65536 이므로 17 (0~16)이면 충분합니다.
LOG_MAX = 17 

# 1. 자료구조 초기화
# 트리를 인접 리스트로 표현
graph = [[] for _ in range(N + 1)]
# 각 노드의 깊이
depth = [0] * (N + 1)
# 각 노드의 방문 여부 (DFS용)
visited = [False] * (N + 1)
# parent[i][j] : 노드 i의 2^j 번째 조상
parent = [[0] * LOG_MAX for _ in range(N + 1)]

# N-1개의 간선 정보를 입력받아 그래프 구성
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 2. 전처리 1: DFS를 통해 깊이와 직계 부모 계산
def dfs(node, d):
    """
    깊이 우선 탐색을 수행하며 각 노드의 깊이와 직계 부모(2^0 조상)를 기록합니다.
    node: 현재 노드
    d: 현재 노드의 깊이
    """
    visited[node] = True
    depth[node] = d
    for neighbor in graph[node]:
        if not visited[neighbor]:
            # neighbor의 직계 부모는 node
            parent[neighbor][0] = node
            dfs(neighbor, d + 1)

# 3. 전처리 2: 이진 리프팅 테이블(parent 배열) 채우기
def set_parent():
    """
    모든 노드에 대해 2^j 번째 조상을 계산하여 parent 테이블을 채웁니다.
    """
    # 먼저 DFS를 실행하여 depth와 2^0 조상을 설정
    dfs(1, 0) # 루트 노드 1번, 깊이 0
    
    # 2^1 부터 2^(LOG_MAX-1) 번째 조상까지 계산
    for j in range(1, LOG_MAX):
        for i in range(1, N + 1):
            # i의 2^j 조상 = (i의 2^(j-1) 조상)의 2^(j-1) 조상
            parent[i][j] = parent[ parent[i][j-1] ][ j-1 ]

# 4. 쿼리 함수: LCA(a, b) 계산
def lca(a, b):
    """
    이진 리프팅을 사용하여 두 노드 a와 b의 최소 공통 조상을 찾습니다.
    """
    
    # 1단계: 깊이 맞추기 (b가 항상 더 깊도록 설정)
    if depth[a] > depth[b]:
        a, b = b, a
        
    # 2단계: b를 a와 같은 깊이로 올리기
    # 큰 점프(2^i)부터 확인하며 b를 위로 이동
    for i in range(LOG_MAX - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]
            
    # 3단계: 조상 확인 (깊이를 맞췄더니 두 노드가 같다면, a가 b의 조상이었음)
    if a == b:
        return a
        
    # 4단계: 두 노드 동시에 올리기
    # a와 b의 2^i 조상이 다를 경우에만 위로 이동
    # (같다면, 그 조상이 LCA이거나 LCA보다 위쪽이므로 건너뜀)
    for i in range(LOG_MAX - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
            
    # 5단계: LCA 반환
    # 4단계를 거치면 a와 b는 LCA의 바로 아래 자식 노드가 됨
    # 따라서 a (또는 b)의 직계 부모가 LCA
    return parent[a][0]

# --- 메인 로직 실행 ---

# 1. 전처리 실행
set_parent()

# 2. 쿼리(Q) 수 입력
Q = int(input())

# 3. Q개의 쿼리 처리
for _ in range(Q):
    a, b = map(int, input().split())
    # LCA 계산 및 출력
    print(lca(a, b))