from sortedcontainers import SortedSet
n = int(input())
s = SortedSet()
for _ in range(n):
    p, l = map(int, input().split())
    s.add((l, p))

m = int(input())
commands = []
for _ in range(m):
    cmd = input().split()
    if cmd[0] == "rc":
        if cmd[1] == '1':
            print(s[-1][1])
        else:
            print(s[0][1])
    elif cmd[0] == 'ad':
        s.add((int(cmd[2]), int(cmd[1])))
    elif cmd[0] == 'sv':
        s.remove((int(cmd[2]), int(cmd[1])))
