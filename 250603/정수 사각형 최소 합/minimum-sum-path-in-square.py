import copy
# Please write your code here.

def is_range(x,y,n):
    return 0<=x<n and 0<=y<n

def main(n):
    board = copy.deepcopy(grid)
    for row in range(n):
        for col in range(n-1,-1,-1):
            if is_range(row-1,col,n):
                if board[row][col] == grid[row][col]:
                    board[row][col] = board[row-1][col]+grid[row][col]
                else:
                    board[row][col] = min(board[row][col], board[row-1][col]+grid[row][col])
            
            if is_range(row,col-1,n):
                if board[row][col-1] == grid[row][col-1]:
                    board[row][col-1] =  board[row][col]+grid[row][col-1]
                else:
                    board[row][col-1] = min(board[row][col-1], board[row][col]+grid[row][col-1])
            
    
    print(board[n-1][0])


if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    main(n)