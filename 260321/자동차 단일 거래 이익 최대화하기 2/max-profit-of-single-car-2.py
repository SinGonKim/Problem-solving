n = int(input())
arr = list(map(int, input().split()))
# Please write your code here.
ans = 0
min_stack = []


for x in arr:
    while min_stack:
        y = min_stack.pop()
        if y >= x: continue
        else:
            min_stack.append(y)
            break
    if min_stack:
        ans = max(ans, x - min_stack[-1])
    else:
        min_stack.append(x)
print(ans)
        