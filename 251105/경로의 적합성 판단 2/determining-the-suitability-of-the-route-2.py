import sys
from collections import defaultdict, deque

# 입력 속도를 위해 sys.stdin.readline 사용
input = sys.stdin.readline
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
    
    current_node = order[0]
    
    # 1부터 k-1까지 (다음 목적지)
    for i in range(1, k):
        target_node = order[i]
        
        # current_node에서 target_node로 가는 경로가 있는지
        # '이번 탐색'에서만 사용할 visited 셋
        visited_segment = {current_node}
        q = deque([current_node])
        found = False
        
        while q:
            node = q.popleft()
            
            # 목적지 도달!
            if node == target_node:
                found = True
                break
                
            for neighbor in graph[node]:
                # 이번 탐색에서 방문한 적이 없다면
                if neighbor not in visited_segment:
                    visited_segment.add(neighbor)
                    q.append(neighbor)
        
        # 큐가 비었는데도 못 찾았다면 (경로가 없다면)
        if not found:
            print(0)
            return
            
        # 찾았다면, 다음 탐색을 위해 현재 위치를 갱신
        current_node = target_node

    # 모든 순서를 통과했다면
    print(1)

if __name__ == "__main__":
    solve()