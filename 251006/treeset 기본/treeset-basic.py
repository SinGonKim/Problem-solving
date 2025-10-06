n = int(input())
from sortedcontainers import SortedSet
s = SortedSet()
for _ in range(n):
    line = input().split()
    com = line[0]
    if com == 'add':
        s.add(int(line[1]))  # 정수로 변환!
    elif com == 'remove':
        s.remove(int(line[1]))  # 정수로 변환!
    elif com == 'find':
        if int(line[1]) in s:  # 정수로 변환!
            print('true')
        else:
            print('false')
    elif com == 'lower_bound':
        idx = s.bisect_left(int(line[1]))  # 정수로 변환!
        if idx < len(s):
            print(s[idx])
        else:
            print("None")
    elif com == 'upper_bound':
        idx = s.bisect_right(int(line[1]))  # 정수로 변환!
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