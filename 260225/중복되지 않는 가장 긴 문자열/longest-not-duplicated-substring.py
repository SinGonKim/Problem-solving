from collections import deque
word = input()

# Please write your code here.

que = deque()

for w in word:
    if len(que):
        s = que[-1]
        if w == s: continue
        elif w in s:
            que.append(w)
        else:
            ns = s + w
            que.pop()
            que.append(ns)
    else:
        que.append(w)

answer = 0

while que:
    s = que.popleft()
    answer = max(answer, len(s))
print(answer)
