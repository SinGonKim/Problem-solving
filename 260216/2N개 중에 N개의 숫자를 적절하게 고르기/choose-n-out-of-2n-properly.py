import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:

n = int(input())
num = list(map(int, input().split()))
visited = [False for _ in range(2 * n)]

ans = INT_MAX


def calc():
    diff = 0
    for i in range(2 * n):
        diff = (diff + num[i]) if visited[i] else diff - num[i]
    
    return abs(diff)


def find_min(idx, cnt):
    global ans
    
    if cnt == n:
        ans = min(ans, calc())
        return
    
    if idx == 2 * n:
        return
    
    # 현재 숫자를 첫 번째 그룹에 사용한 경우입니다.
    visited[idx] = True
    find_min(idx + 1, cnt + 1)
    visited[idx] = False
    
    # 현재 숫자를 두 번째 그룹에 사용한 경우입니다.
    find_min(idx + 1, cnt)
    

find_min(0, 0)
print(ans)
