n = int(input())
x = [int(input()) for _ in range(n)]

# Please write your code here.
import heapq
heap = []

for s in x:
    if s != 0:
        heapq.heappush(heap, -s)
    elif s == 0:
        if len(heap):
            print(-heapq.heappop(heap))
        else:
            print(0)