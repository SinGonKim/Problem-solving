n, k = map(int, input().split())
bomb = []

for i in range(n):
    bomb_num = int(input())
    bomb.append((bomb_num, i))

answer = -1

# 내림차순 정렬 (폭탄 번호 기준)
bomb.sort(reverse=True)

for i in range(1, len(bomb)):
    bomb_num = bomb[i][0]
    if bomb[i-1][0] == bomb_num:
        dist = bomb[i-1][1] - bomb[i][1]
        if dist <= k:
            answer = bomb_num
            break

print(answer)