n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
left = 1
right = sum(arr) // m # right이 (전체 합/m) 값보다는 작아야 한다. ex. 예제 답은 200이나 전체 합/11 = 231

import sys
ans = -sys.maxsize

def is_possible(target):
    cnt = m
    for elem in arr:
        if elem >= target:
            cnt -= (elem // target)

    return cnt <= 0


while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1
print(max(ans,0))