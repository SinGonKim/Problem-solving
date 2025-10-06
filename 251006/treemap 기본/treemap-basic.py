from sortedcontainers import SortedDict
n = int(input())

cmd = []
sd = SortedDict()

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] == "add":
        sd[int(line[1])] = int(line[2])
    elif line[0] == "remove":
        del sd[int(line[1])]    
    elif line[0] == "find":
        if int(line[1]) in sd.keys():
            print(sd[int(line[1])])
        else:
            print("None")
    else:
        if len(sd):
            for k, v in sd.items():
                print(v, end = ' ')
            print()
        else:
            print("None")

# Please write your code here.
