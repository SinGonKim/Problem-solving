import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
def multi(a,b):
    if b == 1:
        return a%c
    else:
        v = multi(a,b//2) #곱셈 분해 ex) 10**5를 (10**2)*(10**2)*(10*2) 로 나누겠다는 의미이다.
        if b%2 == 0:
            return (v*v)%c
        else:
            return (v*v*a)%c
print(multi(a,b))
