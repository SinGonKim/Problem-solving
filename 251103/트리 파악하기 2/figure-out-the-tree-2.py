n = int(input())
words = []

for _ in range(n):
    _, *chars = tuple(input().split())
    words.append("".join(chars))

class Trie():
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

root = Trie()

def insert_word(s):
    t = root
    for char in s:
        index = ord(char) - ord('A')
        if t.children[index] is None:
            t.children[index] = Trie()
        t = t.children[index]
    t.is_end =True

def print_trie(node, depth):
    for index in range(26):
        if node.children[index]:
            print('-'*(2*depth) + chr(ord('A') + index))
            print_trie(node.children[index], depth+1)

for word in words:
    insert_word(word)
print_trie(root,0)