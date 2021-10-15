import sys
input =sys.stdin.readline
N, X = map(int, input().split())
A = list(map(int,input().split()))
B = []
for i in A:
    if i < X:
        B.append(str(i))
answer = " ".join(B)
print(answer)
