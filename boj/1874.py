from collections import deque
import sys
input = sys.stdin.readline

if __name__ =="__main__":
    n = int(input())
    deq = deque()
    ans = []
    target = 0
    for _ in range(n):
        num = int(input())
        while num-target>0:
            target +=1
            deq.append(target)
            ans.append('+')
        if target >= num:
            x = deq.pop()
            if x != num:
                break
            else:
                ans.append('-')
    if len(deq) == 0:
        for i in ans:
            print(i)
    else:
        print('NO')
