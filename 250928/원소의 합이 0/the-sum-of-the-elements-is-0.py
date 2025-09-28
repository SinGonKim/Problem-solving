n = int(input())
num = [list(map(int, input().split())) for _ in range(4)]

dic = {}
dic2 = {}
cnt = 0

# Please write your code here.

for i in range(n):
    for j in range(n):
        if num[0][i] + num[1][j] not in dic:
            dic[num[0][i] + num[1][j]] = 1
        else:
            dic[num[0][i] + num[1][j]] += 1

        if num[2][i] + num[3][j] not in dic2:
            dic2[num[2][i] + num[3][j]] = 1
        else:
            dic2[num[2][i] + num[3][j]] += 1

for key, value in dic.items():
    for key1, value1 in dic2.items():
        if key + key1 == 0:
            cnt += value*value1

print(cnt) 