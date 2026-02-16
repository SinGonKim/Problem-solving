n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
import sys
sys.setrecursionlimit(10**6)
answer = sys.maxsize

def solve(idx, total, left, right):
    global answer

    if idx == 2*n:
        answer = min(answer, abs(total))
        return
    if left < n:
        solve(idx+1, total+num[idx], left+1, right)
    if right < n:
        solve(idx+1, total-num[idx], left, right+1)


solve(0, 0, 0, 0)
print(answer)