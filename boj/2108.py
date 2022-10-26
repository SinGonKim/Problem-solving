import sys
input= sys.stdin.readline
n = int(input())
s = 0
A = []
for _ in range(n):
    x = int(input())
    s += x
    A.append(x)
print(round(s/n)) #산술평균 반올림함수 round
A.sort()
print(A[(n//2)]) # 중앙값
## 최빈값 구하기
B = dict() #딕셔너리 정의
for i in range(1, n+1):
    B[i] = [] #1번 나오는 것부터 n번까지 숫자 넣기 작전
if n==1: # n이 한번인 경우
    B[1].append(A[0]) #하나 넣는다.
else:
    cnt = 1
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            cnt += 1
            if i+1 == len(A)-1:
                B[cnt].append(A[i])
        else:
            B[cnt].append(A[i])
            cnt = 1
for j in range(n,0,-1):
    if len(B[j])==0:
        continue
    elif len(B[j]) ==1:
        print(B[j][0])
        break
    else:
        print(B[j][1])
        break
# print(max(B, key=B.get)) #최빈값 dict values()최댓값인 key 찾기 key = B.get
print(A[-1]-A[0]) #범위
