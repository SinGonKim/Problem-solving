import sys
input = sys.stdin.readline
def solve(start):
    global P
    for road in C[:]:
        if start == road[0] and road[1] not in P:
            P.append(road[1])
            solve(road[1])
            C.remove(road)
            C.remove([road[1],road[0]])
    return
if __name__=="__main__":
    n = int(input())
    C = [] #초기 로드
    P = [1] #감염된 컴퓨터
    for _ in range(int(input())):
        a, b = map(int, input().split())
        C.append([a,b])
        C.append([b,a])
    solve(1)
    print(len(set(P))-1)
