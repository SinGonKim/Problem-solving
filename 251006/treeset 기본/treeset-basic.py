n = int(input())
from sortedcontainers import SortedSet
s = SortedSet()
for _ in range(n):
    line = input().split()
    com = line[0]
    if com == 'add':
        s.add(line[1])
    elif com == 'remove':
        s.remove(line[1])
    elif com == 'find':
        if line[1] in s:
            print('true')
        else:
            print('false')
    elif com == 'lower_bound':
        idx = s.bisect_left(line[1])
        if idx < len(s):
            print(s[idx])
        else:
            print("None")
    elif com == 'upper_bound':
        idx = s.bisect_right(line[1])
        if idx < len(s):
            print(s[idx])
        else:
            print("None")
    elif com == 'largest':
        if len(s):
            print(s[-1])
        else:
            print("None")
    elif com == 'smallest':
        if len(s):
            print(s[0])
        else:
            print("None")