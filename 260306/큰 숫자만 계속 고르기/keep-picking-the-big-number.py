import heapq
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
heap = []
for x in arr:
    heapq.heappush(heap, -x)

for _ in range(m):
    x = -heapq.heappop(heap)
    heapq.heappush(heap,-(x-1))
print(-heap[0])