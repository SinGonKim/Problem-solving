import sys
input = sys.stdin.readline
from collections import deque
def solve():
    for i in range(1,n+1):
        while len(que):
            x = que.pop()
            if B[A[-i]] < B[x]:
                ans.append(x)
                que.append(x)
                break
        if len(que)==0:
            ans.append(-1)
        que.append(A[-i])
    ans.reverse()
    print(*ans)
    return
if __name__=="__main__":
    n = int(input())
    A = list(map(int, input().split()))
    B = dict()
    for i in A:
        if i in B.keys():
            B[i] += 1
        else:
            B[i] = 1
    que = deque()
    ans = []
    solve()
