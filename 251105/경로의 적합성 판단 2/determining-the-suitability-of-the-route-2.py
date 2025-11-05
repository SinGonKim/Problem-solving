import sys
# 재귀 깊이 제한을 늘려줍니다. (Union-Find의 find 연산 때문)
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# find 연산 (경로 압축 적용)
def find_parent(parent, x):
    if parent[x] == x:
        return x
    # 재귀적으로 부모를 찾으면서, 찾은 루트로 부모를 갱신 (경로 압축)
    parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산 (두 원소가 속한 집합 합치기)
def union_parent(parent, a, b):
    rootA = find_parent(parent, a)
    rootB = find_parent(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

def solve():
    n, m, k = map(int, input().split())
    
    # 1. 부모 테이블 초기화
    parent = [i for i in range(n + 1)]
    
    # 2. 모든 간선에 대해 union 연산 수행 (그래프의 연결 요소 구성)
    for _ in range(m):
        u, v = map(int, input().split())
        union_parent(parent, u, v)
        
    order = list(map(int, input().split()))
    
    # k=1 이면 항상 가능
    if k == 1:
        print(1)
        return

    # 3. order 순서대로 연결성 확인
    for i in range(k - 1):
        current_node = order[i]
        next_node = order[i+1]
        
        # 4. 두 노드의 루트(최상위 부모)가 다른지 확인
        if find_parent(parent, current_node) != find_parent(parent, next_node):
            print(0)  # 연결되어 있지 않음 (이동 불가)
            return
            
    # 5. 모든 순서가 연결되어 있음
    print(1)

if __name__ == "__main__":
    solve()