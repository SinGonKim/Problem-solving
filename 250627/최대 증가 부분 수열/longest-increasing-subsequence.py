n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
import bisect

stack = []
stack.append(m[0])

for i in range(1,n):
    idx = bisect.bisect_left(stack,m[i])
    if idx == len(stack):
        stack.append(m[i])
  
    else:
        stack[idx] = m[i]
     
 
print(len(stack))

