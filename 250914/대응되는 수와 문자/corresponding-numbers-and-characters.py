n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.
word2idx = dict()
for idx, word in enumerate(words):
    word2idx[word] = idx

for q in queries:
    if q.isdigit():
        print(words[int(q)])
    else:
        print(word2idx[q])