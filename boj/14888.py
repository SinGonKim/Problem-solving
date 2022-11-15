import sys
input = sys.stdin.readline
def dfs(depth, total, plus, minus, multiply, divide):
    global ans
    if depth ==  n:
        ans[0] = max(total, ans[0]) 
        ans[1] = min(total, ans[1])
        return
    if plus:
        dfs(depth+1, total+A[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total-A[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total*A[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total/A[depth]), plus, minus, multiply, divide-1)        
if __name__=="__main__":
    n = int(input())
    A = list(map(int, input().split()))
    Calculator = list(map(int, input().split()))
    ans = [-1000000000,10000000000]
    dfs(1, A[0], Calculator[0],Calculator[1], Calculator[2], Calculator[3])
    print(ans[0])
    print(ans[1])
