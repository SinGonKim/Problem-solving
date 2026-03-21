import heapq

n = int(input())
total = {i for i in range(1, 2*n+1)}
answer = 0

b = [int(input()) for _ in range(n)]
a = list(total - set(b))

heapq.heapify(b)
heapq.heapify(a)

temp = heapq.heappop(b)

while True:
    x = heapq.heappop(a)
    if x > temp:
        answer += 1
        if len(b) and len(a):
            temp = heapq.heappop(b)
        else:
            break
print(answer)