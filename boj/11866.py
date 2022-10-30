from collections import deque
import sys
input = sys.stdin.readline

if __name__ =="__main__":
    n, k = map(int, input().split())
    deq = deque()
    ans = []
    for i in range(1,n+1):
        deq.append(i)
    while len(deq)>0:
        for _ in range(k-1):
            deq.append(deq.popleft())
        ans.append(deq.popleft())
    print('<', end = '')
    print(', '.join(map(str, ans)), end='') #리스트 안의 숫자의 type을 int에서 str으로 바꿔서 join
    print('>')
