n = int(input())
X = [int(input()) for _ in range(n)]

# Please write your code here.
import heapq
import sys
INF = sys.maxsize
p_heap = []
m_heap = []

for x in X:
    if x > 0:
        heapq.heappush(p_heap, x)
    elif x < 0:
        heapq.heappush(m_heap, -x)
    else:
        if len(p_heap) == 0 and len(m_heap) == 0:
            print(0)
        elif len(m_heap) == 0:
            p = heapq.heappop(p_heap)
            print(p)
        elif len(p_heap) == 0:
            m = -heapq.heappop(m_heap)
            print(m)
        else:
            p = heapq.heappop(p_heap)
            m = -heapq.heappop(m_heap)
            if p < abs(m):
                print(p)
                heapq.heappush(m_heap, -m)
            else:
                print(m)
                heapq.heappush(p_heap, p)


