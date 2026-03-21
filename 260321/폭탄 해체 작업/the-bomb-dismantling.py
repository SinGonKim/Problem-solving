N = int(input())
# Please write your code here.

answer = 0
t = 1
bombs = []
for i in range(N):
    p, e = map(int, input().split())
    bombs.append((e, -p))
import heapq
heapq.heapify(bombs)

while bombs:
    e, m = heapq.heappop(bombs)
    p = (-1)*(m)
    if t <= e:
        print(p, t)
        answer += p
        t += 1
    else:
        continue
print(answer)