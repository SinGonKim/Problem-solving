import heapq
N = int(input())
people = []
answer = 0
for i in range(1, N+1):
    ai, ti = map(int, input().split())
    people.append((ai, i, ti))

# Please write your code here.
people.sort()

heap = [] # (번호, 도착시간, 머무는 시간)
idx = 0
cur = 0
max_wait = 0

while idx < N or heap:
    if not heap:
        cur = max(cur, people[idx][0])

    while idx < N and people[idx][0] <= cur:
        a, num, stay = people[idx]
        heapq.heappush(heap, (num, a, stay))
        idx += 1
    num, a, stay = heapq.heappop(heap)
    max_wait = max(max_wait, cur - a)
    cur += stay
print(max_wait)