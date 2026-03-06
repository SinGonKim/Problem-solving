N = int(input())
commands = []

for _ in range(N):
    line = input().split()
    if line[0] == "push":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0],))

# Please write your code here.
import heapq
class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, x):
        heapq.heappush(self.heap, -x)
    
    def empty(self):
        return not self.heap
    
    def size(self):
        return len(self.heap)
    
    def pop(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        
        return -heapq.heappop(self.heap)
    
    def top(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        return -self.heap[0]

que = PriorityQueue()
for com in commands:
    if com[0] == "push":
        que.push(com[1])
    elif com[0] == "pop":
        print(que.pop())
    elif com[0] == "size":
        print(que.size())
    elif com[0] == "empty":
        print(1 if que.empty() else 0)
    elif com[0] == "top":
        print(que.top())
