from collections import deque
import sys
input = sys.stdin.readline
while 1:
    height = list(map(int,input().split())) #높이의 리스트
    n = height.pop(0)
    if n ==0: #없으면 종료
        break
    stack = deque() #스택을 이용한 풀이
    answer = 0

    # 왼쪽부터 차례대로 탐색
    for i in range(n):
        while len(stack) != 0 and height[stack[-1]] > height[i]: #i 는 height의 index로 보면 된다. index대로 stack에 넣고 빼고를 볼 것인데 i번째 인덱스의 높이보다 스택에 남아있는 최근 높이가 더 크면 높이의 최고치는 한계가 와서 뽑아 버릴 것이다. index는 x축 좌표, height는 y축 좌표기록이라 보며 되며 index는 i가 있기 때문에 뽑아도 사라지지 않는다.
            tmp = stack.pop() #가장 위 스택을 뽑는다. 이걸 정산할 차례!

            if len(stack) ==0: #스택에 남아있는 것이 없으면
                width = i # 스택에 남아있는 것이 없다는 것은 잘 생각하면 위에 while문을 보듯이 그 전 i에서도 지금 height[tmp] 값보다 커서 stack.pop을 했다는 것을 알 수 있다. 따라서 tmp로 정산할 것은 i*temp이 최대이다.
            else: #스택에 남아있는 것이 있으면
                width = i - stack[-1] -1 #stack[-1]의 높이는 tmp 높이보다 작다는 것을 알 수 있다. 따라서 height[tmp]의 최대 width는 i-(stack[-1] +1)이다. i는 height[tmp]오른쪽 끝의 i이다.
            answer = max(answer, width*height[tmp]) # 그 전의 최댓값과 비교해서 높은 값만 남겨둔다.
        stack.append(i) #stack에 i인덱스를 넣어서 다음거를 맞이한다!
    
    # 스택에 남아있는 것을 처리
    while len(stack) != 0:
        tmp = stack.pop()

        if len(stack) == 0: #그닌까 tmp만 남은거였으면
            width = n #위에서 보듯 나머지는 height[stack[-1]] > height[i]로 다 뺐는데 하나 마지막 push 한 것이다. 따라서 그 전 index의 height보다 낮다는 것을 알 수 있으므로 n*height[tmp]가 될 것이다.
        else:
            width = n-stack[-1] -1 #남아있으면 마지막 잔반처리 (n-(stack[-1]+1))*height[tmp]할것이다.
        answer = max(answer, width*height[tmp])
    print(answer)
