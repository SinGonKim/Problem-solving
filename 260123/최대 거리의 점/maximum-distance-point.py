import sys
n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])

# Please write your code here.
# 이진 탐색 범위 설정
left = 1 # 가능한 최소 거리
right = arr[-1] - arr[0] # 가능한 최대 거리
ans = 0

while left <= right:
    # mid는 '가장 인접한 두 물건 사이의 거리'의 후보입니다.
    mid = (left + right) // 2
    
    # 첫 번째 점에는 무조건 물건을 설치한다고 가정 (그리디)
    count = 1
    last_position = arr[0]
    
    # 현재 mid 거리 이상으로 물건을 몇 개 설치할 수 있는지 체크
    for i in range(1, n):
        if arr[i] - last_position >= mid:
            count += 1
            last_position = arr[i]
            
    # 설치한 물건의 개수가 M개 이상이면, 거리를 더 늘려봅니다.
    if count >= m:
        ans = mid
        left = mid + 1
    # M개 미만으로 설치되면, 거리를 좁혀야 합니다.
    else:
        right = mid - 1

print(ans)