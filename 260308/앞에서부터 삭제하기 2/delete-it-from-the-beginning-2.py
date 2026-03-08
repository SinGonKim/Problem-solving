n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq

heap = []
s = 0
answer = 0

for k in range(n-1,-1,-1):
    num = arr[k]
    heapq.heappush(heap, num)
    s += num

    if len(heap) >= 2 and k > 0:
        temp_sum = s - heap[0]
        avg = temp_sum/(len(heap)-1)

        if avg > answer:
            answer = avg

print(f"{answer:.2f}")
