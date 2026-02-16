n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
import sys
sys.setrecursionlimit(10**6)
answer = sys.maxsize

def solve(idx, total):
    global answer

    if idx == 2*n:
        answer = min(answer, abs(total))
        return
    
    solve(idx+1, total+num[idx])
    solve(idx+1, total-num[idx])


solve(0, 0)
print(answer)