import heapq
n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
heap = []
for idx, x in enumerate(arr):
    heapq.heappush(heap, x)
    if idx < 2:
        print(-1)
        continue
    a1 = heapq.heappop(heap)
    a2 = heapq.heappop(heap)
    a3 = heapq.heappop(heap)
    print(a1*a2*a3)
    heapq.heappush(heap, a1)
    heapq.heappush(heap, a2)
    heapq.heappush(heap, a3)
    


    