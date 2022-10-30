from collections import deque
import sys
input = sys.stdin.readline

if __name__ =="__main__":
    while 1:
        T = input().rstrip()
        if T == ".":
            break
        deq = deque()
        for i in str(T):
            if i== '[' or i == '(':
                deq.append(i)
            elif i ==']':
                if len(deq) !=0 and deq[-1] =='[':
                    deq.pop()
                else:
                    deq.append(']')
                    break
            elif i == ')':
                if len(deq) != 0 and deq[-1] == "(":
                    deq.pop()
                else:
                    deq.append(')')
                    break
        if len(deq) ==0:
            print('yes')
        else:
            print('no')
