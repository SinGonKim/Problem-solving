n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq
heap = []
for x in arr:
    heapq.heappush(heap, -x)

while len(heap) >= 2:
    x1 = -heapq.heappop(heap)
    x2 = -heapq.heappop(heap)
    nx = abs(x1-x2)
    if nx > 0:
        heapq.heappush(heap, -nx)
if len(heap):
    print(-heapq.heappop(heap))
else:
    print(-1)
