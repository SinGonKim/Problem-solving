N = int(input())
# Please write your code here.

answer = 0
t = 1
bombs = []
for i in range(N):
    p, e = map(int, input().split())
    bombs.append((-p, e))
import heapq
heapq.heapify(bombs)
max_limit = max(x[1] for x in bombs)
schedule = [False for _ in range(max_limit+1)]
ans = 0
while bom:
    m_score, limit = heapq.heappop(bombs)
    score = (-1)*m_score
    for d in range(limit,0,-1):
        if not schedule:
            schedule[d] = True
            ans += score
            break
print(ans)