import sys
from collections import deque

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    # 1. 입력 받기 (N: 정점 수, R: 루트, Q: 쿼리 수)
    N, R, Q = map(int, input().split())
    
    # 2. 인접 리스트로 그래프 생성 (양방향)
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        U, V = map(int, input().split())
        graph[U].append(V)
        graph[V].append(U) # (버그 수정: V -> U)
        
    # 3. BFS를 위한 자료구조 초기화
    parent = [0] * (N + 1)      # 각 노드의 부모 노드 저장
    children = [[] for _ in range(N + 1)] # 각 노드의 자식 노드들 저장
    visited = [False] * (N + 1) # 방문 여부
    queue = deque([R])          # BFS 큐
    visited[R] = True
    
    # BFS 탐색 순서를 저장 (루트 -> 리프)
    processing_order = [] 

    # 4. BFS 실행: 부모-자식 관계 설정 및 탐색 순서 저장
    while queue:
        current = queue.popleft()
        processing_order.append(current) # 큐에서 뽑은 순서대로 저장
        
        for neighbor in graph[current]:
            # 아직 방문 안 했고, 부모 노드가 아니라면
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current       # 부모-자식 관계 설정
                children[current].append(neighbor) # 부모-자식 관계 설정
                queue.append(neighbor)           # 큐에 추가
                
    # 5. 서브트리 크기 계산
    #    모든 노드의 크기를 1(자기 자신)로 초기화
    subtree_size = [1] * (N + 1)
    
    # processing_order를 역순으로 순회 (리프 -> 루트)
    for node in reversed(processing_order):
        # 현재 노드가 루트가 아니라면
        if parent[node] != 0:
            # 현재 노드의 서브트리 크기를 부모 노드의 서브트리 크기에 더함
            subtree_size[parent[node]] += subtree_size[node]

    # 6. Q개의 쿼리 처리
    results = []
    for _ in range(Q):
        U = int(input())
        print(subtree_size[U])


# 함수 실행
solve()