S = input()
A = '#' + '#'.join(list(S)) + "#"
# Please write your code here.
n = len(A)
C = [0 for _ in range(n)]

r, p = -1, -1
cnt = 0
for i in range(n):
    if r < i:
        C[i] = 0
    else:
        ii = 2*p - i
        C[i] = min(r-i, C[ii])
    
    while (i - C[i] -1 >=0) and (i + C[i] + 1 < n) and A[i-C[i]-1] == A[i+C[i]+1]:
        C[i] += 1
    cnt += (C[i]+1)//2

    if r < i + C[i]:
        r, p = i + C[i], i

print(cnt)
