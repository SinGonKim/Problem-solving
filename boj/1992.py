import sys
input = sys.stdin.readline

def solution(x,y,n):
    color = int(board[x][y])
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != int(board[i][j]):
                color = -1
                break
    if color == -1: #black과 white가 섞여있다면 4분할해서 재귀
        print("(", end = '')

        solution(x,y,n//2)
        solution(x,y+n//2, n//2)
        solution(x+n//2, y, n//2)
        solution(x+n//2, y+n//2, n//2)
        print(')', end = '')
    elif color == 1: #black으로만 이루어져있으면
        print(1, end ='')
    if color == 0: #white으로만 이루어져있으면
        print(0, end='')
if __name__=="__main__":
    n = int(input()) #몇칸짜리인지 입력
    board = [list(input()) for _ in range(n)] #흑백영상 색부터 입력하자
    # black = 1로 정의
    # white = 0로 정의
    solution(0,0,n)


