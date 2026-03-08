n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq
heap = []
base = 0
for x in arr[n-1:]:
    base += x
    heapq.heappush(heap, x)
stack = -1
answer = 0
for k in range(n-2,-1,-1):
    if stack == -1:
        heapq.heappush(heap, arr[k])
        s = base + arr[k]
        res = heapq.heappop(heap)
        s -= res
        stack = res
    else:
        if stack <= arr[k]:
            heapq.heappush(heap, arr[k])
            s = base + arr[k]
        else:
            heapq.heappush(heap, stack)
            s = base + stack
            stack = arr[k]
    answer = max(answer, s/(n-k-1))
print(f"{answer:.2f}")
