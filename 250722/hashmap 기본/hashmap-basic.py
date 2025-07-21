n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

# Please write your code here.
hashmap = dict()
for cmd in commands:
    if cmd[0] == "add":
        hashmap[cmd[1]] = cmd[2]
    elif cmd[0] == "remove":
        hashmap[cmd[1]] = None
    else:
        if cmd[1] in hashmap.keys():
            print(hashmap[cmd[1]])
        else:
            print("None")
