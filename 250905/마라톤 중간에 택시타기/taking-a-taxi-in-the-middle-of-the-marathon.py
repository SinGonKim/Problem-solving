n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
D = [0]
for i in range(1,n):
    d = abs(x[i]-x[i-1]) + abs(y[i]-y[i-1])
    D.append(d)

L = [0 for _ in range(n)]
R = [0 for _ in range(n)]

for i in range(1,n):
    L[i] = L[i-1] + D[i]
for i in range(n-2,0,-1):
    R[i] = R[i+1] + D[i+1]
import sys

target = sys.maxsize
for i in range(1,n-1):
    target = min(target, L[i-1]+R[i+1]+abs(x[i+1]-x[i-1]) + abs(y[i+1]-y[i-1]))
print(target)

