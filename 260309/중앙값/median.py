t = int(input())
import heapq
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))

    # Please write your code here.
    min_heap = []
    max_heap = []
    results = []

    for i in range(m):
        val = arr[i]

        if not max_heap or val <= -max_heap[0]:
            heapq.heappush(max_heap, -val)
        else:
            heapq.heappush(min_heap, val)
        
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(max_heap) < len(min_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
        if i%2==0:
            results.append(-max_heap[0])
    print(*results)