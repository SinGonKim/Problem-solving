from collections import deque
word = input()

# Please write your code here.

que = deque()

answer = 0

for w in word:
    if len(que):
        s = que[-1]
        if w == s:
            continue
        else:
            x = s.rfind(w)
            if x == -1:
                ns = s + w
            else:
                ns = s[x+1:] + w
            que.append(ns)
    else:
        answer = max(answer, len(w))
        que.append(w)


while que:
    s = que.popleft()
    answer = max(answer, len(s))
print(answer)
