import heapq

n = int(input())
x = [int(input()) for _ in range(n)]
heap = []
# Please write your code here.
for num in x:
    if num > 0:
        heapq.heappush(heap, num)
    elif num == 0:
        if len(heap):
            s = heapq.heappop(heap)
            print(s)
        else:
            print(0)