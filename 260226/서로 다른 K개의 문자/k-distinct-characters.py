word, k = input().split()
k = int(k)

# Please write your code here.
import sys
INF = sys.maxsize

n = len(word)

D = dict()
answer = 0
string = ""
for i in range(n):
    s = word[i]

    if s in D.keys() or len(D.keys()) < k:
        string = string + s
    else:
        min_key = min(D, key = D.get)
        string = word[D[min_key]+1:i] + s
        D.pop(min_key, None)
    D[s] = i
    answer = max(answer, len(string))
print(answer)
