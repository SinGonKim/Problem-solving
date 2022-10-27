import sys
from math import comb
input = sys.stdin.readline
def countNum(N, num):
    count = 0
    divNum = num
    while(N >= divNum):
        count = count + (N//divNum)
        divNum = divNum*num
    return count
if __name__ =="__main__":
    M, N = map(int, input().split())
    print(min(countNum(M,5)-countNum(N,5)-countNum(M-N,5), countNum(M,2)-countNum(N,2)-countNum(M-N,2)))
