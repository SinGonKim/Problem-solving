n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
import sys
answer = sys.maxsize
for k in range(n):
    tmp = 0
    for i, x in enumerate(A):
        tmp += abs(k-i)*x
    answer = min(answer, tmp)
print(answer)