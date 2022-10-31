import sys
input = sys.stdin.readline
def power(adj,n):
    if n==1:
        return adj #행렬 A
    elif n%2:
        return multi(power(adj,n-1), adj)
    else:
        return power(multi(adj,adj), n//2)
def multi(a,b): #행렬끼리 곱
    temp = [[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            s = 0
            for k in range(2):
                s+=a[i][k]*b[k][j]
            temp[i][j] = s%p
    return temp
if __name__ == "__main__":
    n = int(input())
    p = 1000000007
    adj = [[1,1], [1,0]] #Linear Transform Ax=b 에서 b[0]값 뽑으면 됨 A= [[F2,F1], [F1,F0]]
    #피보나치 초기값
    start = [[1],[1]] #F1, F2의 값으로 시작 F0은 사실 필요없으므로
    if n<3: #F1, F2 둘 중 하나라면
        print(1)
    else:
        print(multi(power(adj,n-2), start)[0][0])
