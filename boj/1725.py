import sys
input = sys.stdin.readline
from collections import deque
def solve():
    result = 0
    for i in range(n):
        while que and H[que[-1]] > H[i]:
            height = H[que[-1]]
            que.pop()
            width = i
            if que :
                width = (i - que[-1]-1)
            result = max(result, width*height)
        que.append(i)
    while que:
        height = H[que[-1]]
        que.pop()
        width = n
        if que:
            width = (n-que[-1] -1)
        result = max(result, width*height)
    return result
if __name__=="__main__":
    n = int(input())
    H = []
    for _ in range(n):
        H.append(int(input()))
    que = deque()
    print(solve())
