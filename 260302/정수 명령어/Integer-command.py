T = int(input())
from sortedcontainers import SortedSet
for _ in range(T):
    k = int(input())
    operations = [tuple(input().split()) for _ in range(k)]
    command = [op[0] for op in operations]
    n = [int(op[1]) for op in operations]

    # Please write your code here.

    s = SortedSet()

    for num, com in zip(n, command):
        if com == 'I':
            s.add(num)
        elif len(s) == 0: continue
        else:
            if num == 1:
                s.remove(s[-1])
            else:
                s.remove(s[0])
    
    if len(s):
        print(s[-1], s[0])
    else:
        print("EMPTY")