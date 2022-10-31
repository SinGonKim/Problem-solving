import sys
import heapq
input = sys.stdin.readline

n = int(input())
leftheap = [] #하위 50%
rightheap = [] #상위 50%
answer = []
for i in range(1,n+1):
    num = int(input())
    
    if len(leftheap) == len(rightheap): #개수가 같으면 우선순위는 왼쪽에 먼저 넣는걸로
        heapq.heappush(leftheap, (-num, num)) #추출은 최댓값부터
    else:
        heapq.heappush(rightheap, (num, num))
    #추출은 최솟값부터
    if rightheap and leftheap[0][1] > rightheap[0][0]: #왼쪽 최댓값이 오른쪽 최솟값보다 크면 숫자를 바꿔준다. 
        small = heapq.heappop(rightheap)[0]
        large =heapq.heappop(leftheap)[1]
        heapq.heappush(leftheap, (-small, small))
        heapq.heappush(rightheap, (large, large))

    answer.append(leftheap[0][1]) #왼쪽 최댓값이 정답(중앙값)
for j in answer:
    print(j)



