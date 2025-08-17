#완전탐색

#격자의 크기
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return x<n and y<n and x>=0 and y>=0


dxs = [-1,1,0,0]
dys = [0,0,-1,1]

max_time = 0

#핀볼 게임
#출발점의 위치를 x,y 로 둬보자. 
def play(x,y,d):
    time=1
    while in_range(x,y):
        if arr[x][y]==1:
            d = 3-d
        elif arr[x][y]==2:
            if d<2:
                d = d+2
            else:
                d = d-2
        x,y = x+dxs[d],y+dys[d]
        time+=1

    return time

for i in range(n):
    max_time = max(max_time,play(n-1,i,0))
    max_time = max(play(i,0,3),max_time)
    max_time = max(play(0,i,1),max_time)
    max_time = max(play(i,n-1,2),max_time)

print(max_time)
