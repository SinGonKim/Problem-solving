import sys
input = sys.stdin.readline
c = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)] #색종이 흰곳을 0으로 만든 후 색종이 붙이는 곳을 0으로 만드는 작전!
for _ in range(c):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y,y+10):
            paper[i][j] = 1 # 중복 고려 안해도 된다!
ans = 0
for row in paper:
    ans += row.count(1) #검은 것 개수만 세면 끝!
print(ans)
