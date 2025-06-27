n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
import bisect

stack = []
stack.append(m[0])

for i in range(1,n):
    idx = bisect.bisect_left(stack,m[i])
    if idx == 0:
        stack = [m[i]] + stack
    else:
        stack[idx-1]  = m[i]
print(len(stack))