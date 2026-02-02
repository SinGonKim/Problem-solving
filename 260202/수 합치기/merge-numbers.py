import heapq
n = int(input())
arr = list(map(int, input().split()))
heap = []
# Please write your code here.
for num in arr:
    heapq.heappush(heap, num)

ans = 0
while len(heap) > 1:
    x1 = heapq.heappop(heap)
    x2 = heapq.heappop(heap)
    ans += x1 + x2
    heapq.heappush(heap, x1+x2)
print(ans)