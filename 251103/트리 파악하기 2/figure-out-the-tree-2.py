import sys

# 재귀 깊이 제한 설정
sys.setrecursionlimit(2000)

def solve():
    n = int(sys.stdin.readline())

    # 루트 노드들을 저장할 딕셔너리
    # key: 루트 노드 이름 (e.g., 'A')
    # value: 해당 루트로 시작하는 Trie (중첩 딕셔너리)
    # e.g., {'A': {'B': {'C': {}}, 'D': {}}, 'B': {'A': {}}}
    trees = {}

    for _ in range(n):
        line = sys.stdin.readline().split()
        path = line[1:]  # 노드 경로
        
        if not path:
            continue
            
        root_node = path[0]
        
        # 이 루트 노드가 처음 등장했다면, 딕셔너리에 추가
        if root_node not in trees:
            trees[root_node] = {}
            
        # 루트 노드의 Trie에서부터 탐색 시작
        current_level_dict = trees[root_node]
        
        # 경로의 나머지 노드들을 따라가며 Trie 구성
        for node in path[1:]:
            # 자식이 딕셔너리에 없으면 새로 추가 (빈 딕셔너리)
            if node not in current_level_dict:
                current_level_dict[node] = {}
            
            # 다음 레벨의 딕셔너리(자식)로 이동
            current_level_dict = current_level_dict[node]

    # 트리를 출력하기 위한 DFS 함수
    # node_name: 현재 노드 이름
    # children_dict: 현재 노드의 자식들을 담고 있는 딕셔너리
    # depth: 현재 깊이
    def dfs_print(node_name, children_dict, depth):
        # 깊이에 맞게 '--' 접두사 출력
        print('--' * depth + node_name)
        
        # 자식들을 알파벳 순으로 정렬
        sorted_children = sorted(children_dict.keys())
        
        # 각 자식에 대해 재귀적으로 DFS 수행
        for child_name in sorted_children:
            # grandchild_dict는 child_name의 자식 딕셔너리
            grandchild_dict = children_dict[child_name]
            dfs_print(child_name, grandchild_dict, depth + 1)

    # 루트 노드들을 알파벳 순으로 정렬
    sorted_roots = sorted(trees.keys())
    
    # 각 루트 노드에 대해 DFS 실행
    for root_name in sorted_roots:
        # 루트 노드 출력 (depth 0)
        print(root_name)
        
        root_children_dict = trees[root_name]
        sorted_children = sorted(root_children_dict.keys())
        
        # 루트의 자식들부터 depth 1로 DFS 시작
        for child_name in sorted_children:
            grandchild_dict = root_children_dict[child_name]
            dfs_print(child_name, grandchild_dict, 1)

# 함수 실행
solve()