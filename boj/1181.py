import sys
input= sys.stdin.readline
n = int(input())
l = dict()
for i in range(1, 51):
    l[i] = list()
for _ in range(n):
    word = input().strip() #불순물이 낄 수 있어서 strip은 무조건 문자열에서 써주는 것이 좋다.
    num = len(word)
    l[num].append(word)
for i in range(1,51):
    l[i] = list(set(l[i]))
    l[i].sort()
for i in range(1,51):
    for j in range(len(l[i])):
        print(l[i][j])
