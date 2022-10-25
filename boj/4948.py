import sys
import math
input= sys.stdin.readline
def isprime(n):
    if n ==1:
        return False
    sq = int(math.sqrt(n))
    for i in range(2, sq+1):
        if n%i ==0:
            return False
    return True
ans = []
for num in range(1,300000): #넉넉히 잡아서
    if isprime(num):
        ans.append(num)
while 1:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for num in ans:
        if n < num < 2*n+1:
            cnt +=1
    print(cnt)
