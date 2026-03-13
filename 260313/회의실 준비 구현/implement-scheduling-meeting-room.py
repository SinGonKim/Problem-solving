n = int(input())
meetings = sorted([tuple(map(int, input().split())) for _ in range(n)])

# Please write your code here.
stack = []

for meet in meetings:
    if len(stack) == 0:
        stack.append(meet)
    else:
        while stack:
            if stack[-1][0] <= meet[0] and meet[1] <= stack[-1][1]:
                stack.pop()
            else:
                break
        stack.append(meet)
print(len(stack))

