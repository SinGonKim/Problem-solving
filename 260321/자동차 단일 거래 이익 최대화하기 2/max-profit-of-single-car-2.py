n = int(input())
arr = list(map(int, input().split()))
# Please write your code here.
ans = 0
from collections import deque
max_stack = []


for x in arr:
    while max_stack:
        y = max_stack.pop()
        if y <= x: continue
        else:
            max_stack.append(y)
            break
    if max_stack:
        ans = max(ans, max_stack[-1] - x)
    else:
        max_stack.append(x)
print(ans)
        