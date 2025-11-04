n, m = map(int, input().split())
words = input().split()
S = input()

# Please write your code here.
class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
        self.count = 0

root = TrieNode()

def insert_word(s):
    t = root

    for char in s:
        index = ord(char) - ord('a')
        if t.children[index] is None:
            t.children[index] = TrieNode()
        
        t = t.children[index]
        t.count += 1
    t.is_end = True
    
def search_word(s):
    t = root
    for char in s:
        if t is not None:
            index = ord(char) - ord('a')
            t = t.children[index]
        
        if t is not None:
            print(t.count, end = ' ')
        else:
            print(0, end = ' ')


for word in words:
    insert_word(word)

search_word(S)
