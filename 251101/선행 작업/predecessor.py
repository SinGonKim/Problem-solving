import sys
from collections import deque

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    n = int(input())

    # 그래프 (인접 리스트), 진입 차수(in-degree), 작업 시간
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    times = [0] * (n + 1)
    
    # max_prereq_finish[i]: i번 작업의 선행 작업 중 가장 늦게 끝나는 시각
    max_prereq_finish = [0] * (n + 1)
    
    # finish_times[i]: i번 작업이 최종적으로 완료되는 시각
    finish_times = [0] * (n + 1)

    # 1. 그래프 및 관련 정보 초기화
    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        times[i] = line[0]
        in_degree[i] = line[1]
        
        for prereq in line[2:]:
            # prereq -> i 방향의 간선 추가
            graph[prereq].append(i)

    # 2. 위상 정렬을 위한 큐 초기화
    q = deque()
    for i in range(1, n + 1):
        # 진입 차수가 0인(선행 작업이 없는) 작업
        if in_degree[i] == 0:
            q.append(i)
            # 선행 작업이 없으므로, 완료 시각 = 자신의 작업 시간
            finish_times[i] = times[i]

    # 3. 위상 정렬 수행
    while q:
        current_task = q.popleft()
        
        # current_task를 선행 작업으로 가지는 다음 작업들 확인
        for next_task in graph[current_task]:
            
            # next_task는 current_task가 끝나야 시작 가능
            # next_task의 시작 시간은 모든 선행 작업이 끝난 시간 중 최대값
            # max_prereq_finish를 갱신
            max_prereq_finish[next_task] = max(
                max_prereq_finish[next_task], 
                finish_times[current_task]
            )
            
            # 선행 작업 하나 완료
            in_degree[next_task] -= 1
            
            # next_task의 모든 선행 작업이 완료되었다면
            if in_degree[next_task] == 0:
                # next_task의 최종 완료 시각을 계산
                finish_times[next_task] = max_prereq_finish[next_task] + times[next_task]
                # 큐에 추가하여 다음 작업들 처리
                q.append(next_task)

    # 4. 모든 작업의 완료 시각 중 최댓값 출력
    print(max(finish_times))

# 함수 호출
solve()