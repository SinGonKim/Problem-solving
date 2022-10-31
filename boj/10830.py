import sys
input = sys.stdin.readline

def mul(U, V):
    n = len(U)
    Z = [[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            Z[row][col] = e%1000
    return Z

def square(A, B):
    if B == 1: #그냥 A 출력
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    tmp = square(A, B//2) #분해정리
    if B % 2: #홀수번 곱
        return mul(mul(tmp, tmp),A)
    else: #짝수 제곱수
        return mul(tmp, tmp)
if __name__ =="__main__":
    n, b = map(int, input().split()) #square matrix의 행열개수, b번 곱한다다는 수 입력
    A = [list(map(int, input().split())) for _ in range(n)] #행렬 A 입력
    result = square(A, b)
    for r in result:
        print(*r)
