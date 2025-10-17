
def DFS(x):
    for y in graph[x]:
        if visited[y]:
            continue
        visited[y]=True
        DFS(y)
    
    return 


if __name__=="__main__":
    m=int(input())
    root = 0            # 루트 노드 
    is_tree = True
    
    MAX_N = 10_000      # 최대 노드 개수 
    graph = [[] for _ in range(MAX_N+1)]
    visited = [False]*(MAX_N+1)
    used = [False]*(MAX_N+1)
    arr = [0]*(MAX_N+1)
    for _ in range(m):
        x,y=map(int, input().split())
        graph[x].append(y)
        used[x]=True
        used[y]=True
        arr[y] += 1 # 진입차수, 노드별 들어오는 간선의 개수 
        

    
    # 1. 루트 노드를 찾는다. "들어오는 간선이 하나도 없는 노드"가 여러개 이면 트리가 아니다
    # for문을 통해 모든 노드들을 확인 
    for node in range(1, MAX_N+1):
        if used[node]==True and arr[node]==0:   # node번호가 사용되는데 이 노드로 진입을 안해 
            if root != 0:
                is_tree = False 

            root=node
            
    # 1.1 루트 노드가 없으면 트리가 아니다 
    if root == 0:
        is_tree=False
        

    # 2. 루트 노드를 제외한 다른 노드들로 들어오는 간선은 전부 1개씩이어야만 한다.
    for node in range(1,MAX_N+1):
        # 사용되고 root가 아닌 노드인데 진입차수가 1이 아닌 노드(즉, 진입차수가 2이상)인 거가 있으면 트리 아님 
        if used[node]==True and node != root and arr[node] != 1:
            is_tree = False
    
    # 좋아 위 조건을 만족해서 일단 Tree라고 치면
    # 3. root 노드로부터 모든 노드로 갈 수 있는지 판단해야 한다. 
    if is_tree and root != 0:
        visited[root]=True      # root 노드를 시작으로  
        DFS(root)               # 연결된 모든 노드 visited를 True로 바꿔줌 
    
    for node in range(1, MAX_N+1):
        # node 번호가 사용은 되는데 방문한적이 없다? -> 트리 아님 
        if used[node]==True and visited[node]==False:
            is_tree = False
    
    if is_tree:
        print(1)
    else:
        print(0)