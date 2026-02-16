n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys
sys.setrecursionlimit(10**6)
def solution(idx:int, cnt:int, max_distance:int):
    global answer
    if cnt == m:
        answer = min(answer, max_distance if max_distance != 0 else sys.maxsize)
        return
    elif idx == n:
        return
        
    solution(idx+1, cnt, max_distance) # idx번째 포인터 패스
    target = points[idx]
    if stacks:
        for stack in stacks:
            dist = ((target[0]-stack[0])**2 + (target[1]-stack[1])**2)
            if dist > max_distance:
                max_distance = dist
    stacks.append(target)
    solution(idx+1, cnt+1, max_distance)
    stacks.pop()

answer = sys.maxsize
stacks = []
solution(0, 0, 0)
print(answer)