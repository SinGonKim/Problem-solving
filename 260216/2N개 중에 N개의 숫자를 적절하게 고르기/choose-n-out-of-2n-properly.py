n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
import sys
answer = sys.maxsize

def solve(idx, left, right):
    global answer
    
    if idx == 2*n:
        answer = min(answer, abs(left-right))
        return
    
    solve(idx+1, left+num[idx], right)
    solve(idx+1, left, right+num[idx])


solve(0, 0, 0)
print(answer)