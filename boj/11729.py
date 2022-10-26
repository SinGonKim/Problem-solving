import sys
input = sys.stdin.readline
def F(n):
    if n==1:
        return 1
    elif n == 2:
        return 3
    else:
        return 2*F(n-1)+1
def S(n, start, end):
    if n==1:
        print(start, end)
        return
    S(n-1, start, 6-start-end) #1단계
    print(start, end) #2단계
    S(n-1, 6-start-end, end) #3단계

    # n이 몇이든 간에 우선 (n-1)개를 2로 다 옮기고 n을 3으로 옮긴 후 (n-1)개를 다시 3에 옮기는 것은 똑같다. 그런데 (n-1)개를 1에서 2로 옮기는 과정도 (n-2)개를 1에서 3으로 옮긴 후 n-1을 2로 옮긴 후 (n-2)개를 3에서 2로 옮기는 것과 같다. 이를 재귀에 재귀를 하면 머리는 복잡하지만 순서가 돌아감을 알 수 있을 것이다. (S의 1단계)X n 끝낸후 (S의 1단계) X (n-1) 의 2단계 끝내고 (S의 1단계) X (n-1) 의 3단계 끝낸후 (S의 1단계)X(n-1) ..... 계속 반복될 것이다. 


if __name__ == "__main__":
    n = int(input())
    print(F(n))
    S(n,1,3)
