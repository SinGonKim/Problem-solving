from itertools import combinations

n, m = map(int, input().split()) # 한줄에 M개, 종이가 2*N장 (A그룹, B그룹)

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

# Please write your code here.
idx = [i for i in range(m)]
cnt = 0

for comb in combinations(idx, 3):
    stack = set()
    for i in range(n):
        string = A[i]
        s = string[comb[0]] + string[comb[1]] + string[comb[2]]
        stack.add(s)
    
    for i in range(n):
        string = B[i]
        s = string[comb[0]] + string[comb[1]] + string[comb[2]]
        if s in stack:
            break
    else:
        cnt += 1
print(cnt)
