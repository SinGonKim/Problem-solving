import copy

def toggle(temp_board, r, c): # 주변 숫자 스위칭
    
    # Directions for toggling: self, up, down, left, right
    dr = [0, 0, 0, 1, -1]
    dc = [0, 1, -1, 0, 0]

    for i in range(5):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            temp_board[nr][nc] = 1 - temp_board[nr][nc]


def main():
    min_clicks = float('inf')
    # Iterate through all 2^m possibilities for the first row
    for mask in range(1 << m):
        temp_board = copy.deepcopy([row for row in board])
        current_clicks = 0
        
        # Step 1: Apply clicks to the first row based on the bitmask
        for j in range(m):
            if (mask >> j) & 1:
                toggle(temp_board, 0, j)
                current_clicks += 1
        
        # Step 2: For rows 0 to n-2, if a cell is 0, click the cell below it
        for i in range(n-1):
            for j in range(m):
                if temp_board[i][j] == 0:
                    toggle(temp_board, i + 1 , j)
                    current_clicks += 1
        
        # Step 3: Check if the last row is all 1s
        if all(val == 1 for val in temp_board[-1]):
            min_clicks = min(min_clicks, current_clicks)

    # Output the result
    if min_clicks == float('inf'):
        print(-1)
    else:
        print(min_clicks)

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    main()