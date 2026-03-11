class Node:
    def __init__(self, cur):
        self.cur = cur
        self.prev = None
        self.next = None


def insert_prev(cur, val):
    old_prev = cur.prev

    val.prev = old_prev
    val.next = cur
    cur.prev = val

    if old_prev is not None:
        old_prev.next = val


def insert_next(cur, val):
    old_next = cur.next

    val.prev = cur
    val.next = old_next
    cur.next = val

    if old_next is not None:
        old_next.prev = val


def move_prev(cur):
    if cur.prev is not None:
        return cur.prev
    return cur


def move_next(cur):
    if cur.next is not None:
        return cur.next
    return cur


S_init = input().strip()
N = int(input())

S_cur = Node(S_init)

for _ in range(N):
    line = input().split()
    cmd = int(line[0])

    if cmd == 1:
        new_node = Node(line[1])
        insert_prev(S_cur, new_node)
    elif cmd == 2:
        new_node = Node(line[1])
        insert_next(S_cur, new_node)
    elif cmd == 3:
        S_cur = move_prev(S_cur)
    elif cmd == 4:
        S_cur = move_next(S_cur)

    print(S_cur.prev.cur if S_cur.prev else "(Null)", end=' ')
    print(S_cur.cur, end=' ')
    print(S_cur.next.cur if S_cur.next else "(Null)")