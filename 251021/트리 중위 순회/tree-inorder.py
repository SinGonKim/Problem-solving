import sys

# 재귀 깊이 제한을 넉넉하게 설정합니다.
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

K = int(input())
inorder = list(map(int, input().split()))

tree_levels = [[] for _ in range(K)]

def reconstruct_tree(nodes, level):
    
    # Base Case: 더 이상 나눌 노드가 없으면 종료
    if not nodes:
        return

    # 완전 이진 트리의 중위 순회에서 루트는 항상 중앙에 위치합니다.
    mid = len(nodes) // 2
    root_val = nodes[mid]
    
    # 현재 레벨에 루트 노드 값을 추가합니다.
    tree_levels[level].append(root_val)
    
    # 루트의 왼쪽 부분은 왼쪽 서브트리가 됩니다. (레벨 + 1)
    reconstruct_tree(nodes[:mid], level + 1)
    
    # 루트의 오른쪽 부분은 오른쪽 서브트리가 됩니다. (레벨 + 1)
    reconstruct_tree(nodes[mid+1:], level + 1)

# 재귀 함수를 처음 호출합니다.
# 전체 중위 순회 리스트(inorder)와 루트 레벨(0)에서 시작합니다.
reconstruct_tree(inorder, 0)

# K개의 레벨에 대해 저장된 노드들을 한 줄씩 출력합니다.
for level_nodes in tree_levels:
    print(*level_nodes)