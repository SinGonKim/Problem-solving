n, q = map(int, input().split())
S = input()
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.

input_str = "#" + "#".join(S) + "#"
A = [0]*200_001

n = len(input_str)

r, p = -1, -1

for i in range(n):
    if r < i:
        A[i] = 0
    else:
        ii = 2*p - i
        A[i] = min(r-i, A[ii])
    
    while i - A[i] -1 >=0 and i+A[i] + 1 < n and input_str[i-A[i]-1] == input_str[i+A[i]+1]:
        A[i] += 1
    if i + A[i] > r:
        r, p = i + A[i], i

for a, b in queries:

    a -= 1
    b -= 1

    a = 2*a + 1
    b = 2*b + 1
    m = (a+b)//2
    max_len = 2*A[m] + 1
    if max_len >= b-a+1:
        print("Yes")
    else:
        print("No")