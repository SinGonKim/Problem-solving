import sys
input = sys.stdin.readline
n, m = map(int, input().split())
T = []
for _ in range(n):
    row_color = input()
    T.append(row_color)
error = []
for a in range(0, n-7):
    for b in range(0, m-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b,b+8):
                if (i+j)%2 ==0:
                    if T[i][j] != 'W':
                        index1 +=1
                    if T[i][j] != 'B':
                        index2 += 1
                else:
                    if T[i][j] != 'B':
                        index1 +=1
                    if T[i][j] != 'W':
                        index2 +=1
        error.append(min(index1, index2))
print(min(error))
