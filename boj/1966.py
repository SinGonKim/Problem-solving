from collections import deque
import sys
input = sys.stdin.readline

if __name__ =="__main__":
    t= int(input())
    for _ in range(t):
        n, m = list(map(int, input().split())) #갯수, 몇번째가 궁금한가?
        imp = deque(map(int, input().split())) #중요도 순서
        idx = deque(range(len(imp))) #인덱스 붙이기 0,1,2, ... n
        idx[m] = 'target' #target index

        # 순서
        order = 0
        while 1:
            if imp[0] == max(imp):
                order += 1
                # 두번째 if, idx의 첫 번째 값 "target"?
                if idx[0] == "target":
                    print(order)
                    break
                else:
                    imp.popleft() #처리한 것 삭제
                    idx.popleft()
            else:
                imp.append(imp.popleft()) #뒤로 옮기기
                idx.append(idx.popleft())
