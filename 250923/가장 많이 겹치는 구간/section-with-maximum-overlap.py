n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 1. 각 구간을 시작점(+1)과 끝점(-1) 이벤트로 변환합니다.
events = []
for start, end in intervals:
    # 구간의 시작을 +1로 표시합니다.
    events.append((start, 1))
    # 구간의 끝을 -1로 표시합니다.
    events.append((end, -1))

# 2. 이벤트를 좌표 순서대로 정렬합니다.
# 좌표가 같을 경우, 끝점(-1)이 시작점(+1)보다 먼저 오게 됩니다.
events.sort()

max_overlap = 0
current_overlap = 0

# 3. 정렬된 이벤트를 순서대로 처리하며 최대 겹침을 찾습니다.
for coordinate, event_type in events:
    # 현재 겹치는 구간의 수를 업데이트합니다.
    current_overlap += event_type
    
    # 지금까지의 최대 겹침 수와 비교하여 갱신합니다.
    max_overlap = max(max_overlap, current_overlap)

# 4. 최종 결과를 출력합니다.
print(max_overlap)
