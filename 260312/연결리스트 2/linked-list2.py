from typing import List
N = int(input())
Q = int(input())

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Please write your code here.

Nodes: List[Node] = []

for i in range(N):
    node = Node(i+1)
    Nodes.append(node)
        

for _ in range(Q):
    cmd = list(map(int, input().split()))
    c = cmd.pop(0)
    if c == 1:
        idx = cmd[0]
        node = Nodes[idx-1]

        if node.prev is not None and idx > 1:
            node_prev = Nodes[node.prev-1]
            node_prev.next = node.next
        if node.next is not None and idx < N:
            node_next = Nodes[node.next-1]
            node_next.prev = node.prev
        node.prev = None
        node.next = None
            
    elif c == 2:
        idx, jdx = cmd[0], cmd[1]
        cnode = Nodes[idx-1]
        node = Nodes[jdx-1]
        assert node.prev == None and node.next == None, "Not Single Node!!"
        if cnode.prev is not None:
            prev_node = Nodes[cnode.prev-1]
            prev_node.next = jdx
            node.prev = cnode.prev
        cnode.prev = jdx
        node.next = idx

    elif c == 3:
        idx, jdx = cmd[0], cmd[1]
        node = Nodes[jdx-1]
        assert node.prev == None and node.next == None, "Not Single Node!!"
        cnode = Nodes[idx-1]

        if cnode.next is not None:
            next_node = Node(cnode.next)
            next_node.prev = jdx
            node.next = cnode.next
        cnode.next = jdx
        node.prev = idx
    elif c == 4:
        idx = cmd[0]
        node = Nodes[idx-1]
        prev = node.prev if node.prev is not None else 0
        next = node.next if node.next is not None else 0
        print(prev, next)
for i in range(N):
    node = Nodes[i]
    next = node.next if node.next is not None else 0
    print(next, end = ' ')