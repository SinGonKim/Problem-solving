n = int(input())
sequences = sorted([input() for _ in range(n)], key=lambda x: len(x))

# Please write your code here.
class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(10)]

root = TrieNode()

def insert_word(s):
    t = root
    for char in s:
        index = ord(char) - ord('0')
        if t.children[index] is None:
            t.children[index] = TrieNode()
        t = t.children[index]
        if t.is_end:
            return True
    t.is_end = True
    return False
ans = 1
for seq in sequences:
    exist = insert_word(seq)
    if exist:
        ans = 0
        break
print(ans)

