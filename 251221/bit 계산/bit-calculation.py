q = int(input())
commands = []
for _ in range(q):
    line = input().split()
    if line[0] != "clear":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0],))

# Please write your code here.

class bit_calculator:
    def __init__(self):
        self.S = 0
    
    def add(self, num):
        self.S |= (1<<num)
    
    def delete(self,num):
        self.S &= ~(1<<num)
    
    def printing(self, num):
        print((self.S>>num)%2)
    
    def toggle(self, num):
        if (self.S>>num)%2:
            self.delete(num)
        else:
            self.add(num)
    
    def clear(self):
        self.S = 0

S = bit_calculator()
for com in commands:
    if com[0] == 'add':
        S.add(com[1])
    elif com[0] == 'delete':
        S.delete(com[1])
    elif com[0] == 'print':
        S.printing(com[1])
    elif com[0] == 'toggle':
        S.toggle(com[1])
    else:
        S.clear()
    