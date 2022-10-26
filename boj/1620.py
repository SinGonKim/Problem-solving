import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = dict()
for i in range(1,n+1):
    x= str(input()).strip()
    A[i] = x #번호-이름, 이름-번호 한번씩 한다. 그래야 메모리 많이들어도 시간초과 안됨. 참고로 이름은 숫자가 안들어가므로 중복x
    A[x] = i
for _ in range(m):
    x = str(input()).strip()
    try :
        x = int(x)
        print(A[x])
    except:
        print(A[x])
