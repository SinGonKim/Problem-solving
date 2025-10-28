import sys

# N이 최대 100,000이므로 재귀 깊이 제한을 충분히 늘려줍니다.
sys.setrecursionlimit(10**5 + 10) 

# 빠른 입력을 위해 sys.stdin.readline을 사용합니다.
input = sys.stdin.readline

def solve():
    n = int(input())
    
    # adj[i] = i번 노드의 자식 노드 리스트
    adj = [[] for _ in range(n + 1)]
    
    # values[i] = i번 노드의 초기값
    # 1번 노드(루트)는 초기값이 주어지지 않으므로 0으로 둡니다.
    values = [0] * (n + 1)
    
    # 2번 노드부터 N번 노드까지 N-1개의 정보를 읽어들입니다.
    for i in range(2, n + 1):
        t, a, p = map(int, input().split())
        
        # t=1이면 늑대(양수), t=0이면 양(음수)
        if t == 1:
            values[i] = a
        else:
            values[i] = -a
            
        # 부모 p의 자식 리스트에 현재 노드 i를 추가합니다.
        adj[p].append(i)

    # DFS 함수 정의 (후위 순회)
    # current_node의 최종 값을 계산하여 반환합니다.
    def dfs(current_node):
        
        # 1. 자식 노드들로부터 값을 전달받습니다.
        sum_from_children = 0
        for child_node in adj[current_node]:
            # 자식 노드의 최종 값을 재귀적으로 계산합니다.
            child_final_value = dfs(child_node)
            
            # 규칙 적용:
            # 자식의 최종 값이 양수일 경우에만 부모에게 값을 더합니다.
            # (값이 0 이하이면 아무것도 하지 않습니다.)
            if child_final_value > 0:
                sum_from_children += child_final_value
        
        # 2. 현재 노드의 최종 값을 계산합니다.
        # (현재 노드의 초기값) + (자식들로부터 전달받은 값의 합)
        final_value = values[current_node] + sum_from_children
        
        # 3. 계산된 최종 값을 부모 노드에게 반환합니다.
        return final_value

    # 1번 노드(루트)에서 DFS를 시작하여 최종 값을 계산합니다.
    result = dfs(1)
    print(result)

# 함수 실행
solve()