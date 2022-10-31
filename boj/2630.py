import sys
input = sys.stdin.readline

def solution(x,y,n):
    global white, blue
    color = board[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != board[i][j]:
                solution(x,y,n//2)
                solution(x,y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        white +=1
    else:
        blue +=1

if __name__=="__main__":
    n = int(input()) #몇칸짜리인지 입력
    board = [list(map(int, input().split())) for _ in range(n)] #색종이 색부터 입력하자
    blue = 0
    white = 0
    solution(0,0,n)
    print(white)
    print(blue)


