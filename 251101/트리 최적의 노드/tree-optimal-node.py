import sys
from collections import deque

# 재귀 깊이 제한 해제 (DFS를 사용할 경우 필요할 수 있으나, BFS는 괜찮습니다)
# sys.setrecursionlimit(10**6) 

# N이 100,000까지 가능하므로 빠른 입력을 사용합니다.
input = sys.stdin.readline

# 변수 선언 및 입력:
n = int(input())
edges = [[] for _ in range(n + 1)]

# n - 1개의 간선 정보를 입력받아 인접 리스트를 만듭니다.
for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))
    edges[x].append(y)
    edges[y].append(x)

# BFS 함수 정의
# start_node에서 시작하여 가장 먼 노드와 그 거리를 반환합니다.
def bfs(start_node):
    # dist 배열을 -1로 초기화하여 방문 여부(visited) 확인을 겸합니다.
    dist = [-1] * (n + 1)
    q = deque([start_node])
    
    dist[start_node] = 0
    
    max_dist = 0          # 현재까지 발견된 최대 거리
    farthest_node = start_node # 최대 거리 갱신 시의 해당 노드
    
    while q:
        curr_node = q.popleft()
        
        for next_node in edges[curr_node]:
            # 아직 방문하지 않은 노드라면
            if dist[next_node] == -1:
                dist[next_node] = dist[curr_node] + 1
                q.append(next_node)
                
                # 현재 거리가 최대 거리보다 크다면 갱신
                if dist[next_node] > max_dist:
                    max_dist = dist[next_node]
                    farthest_node = next_node
                    
    return farthest_node, max_dist

# --- 메인 로직 실행 ---

# 1. 임의의 노드(1번)에서 가장 먼 노드(u)를 찾습니다.
u, _ = bfs(1)

# 2. 노드 u에서 가장 먼 노드(v)를 찾습니다.
#    이때 반환되는 최대 거리(max_dist)가 트리의 지름(diameter)입니다.
v, diameter = bfs(u)

# 3. 문제에서 요구하는 값(트리의 반지름)을 계산합니다.
#    반지름 = (지름 / 2)의 올림
#    정수 연산으로는 (diameter + 1) // 2 와 같습니다.
radius = (diameter + 1) // 2

# 4. 결과 출력
print(radius)