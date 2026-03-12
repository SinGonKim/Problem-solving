from typing import List

N = int(input())
Q = int(input())

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None   # 이전 노드 번호
        self.next = None   # 다음 노드 번호

Nodes: List[Node] = [Node(i + 1) for i in range(N)]

for _ in range(Q):
    cmd = list(map(int, input().split()))
    c = cmd[0]

    if c == 1:
        idx = cmd[1]
        node = Nodes[idx - 1]

        if node.prev is not None:
            prev_node = Nodes[node.prev - 1]
            prev_node.next = node.next

        if node.next is not None:
            next_node = Nodes[node.next - 1]
            next_node.prev = node.prev

        node.prev = None
        node.next = None

    elif c == 2:
        idx, jdx = cmd[1], cmd[2]
        cnode = Nodes[idx - 1]
        node = Nodes[jdx - 1]

        # j는 단일 노드라고 문제에서 보장
        if cnode.prev is not None:
            prev_node = Nodes[cnode.prev - 1]
            prev_node.next = jdx
            node.prev = cnode.prev

        node.next = idx
        cnode.prev = jdx

    elif c == 3:
        idx, jdx = cmd[1], cmd[2]
        cnode = Nodes[idx - 1]
        node = Nodes[jdx - 1]

        if cnode.next is not None:
            next_node = Nodes[cnode.next - 1]
            next_node.prev = jdx
            node.next = cnode.next

        node.prev = idx
        cnode.next = jdx

    elif c == 4:
        idx = cmd[1]
        node = Nodes[idx - 1]
        p = node.prev if node.prev is not None else 0
        n = node.next if node.next is not None else 0
        print(p, n)

print(*[(node.next if node.next is not None else 0) for node in Nodes])