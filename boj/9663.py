import sys
n = int(sys.stdin.readline().rstrip())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i): #열이나 대각선라인에 2개 이상 존재하면 안됨
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)
