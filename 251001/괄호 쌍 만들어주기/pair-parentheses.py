A = input()

# Please write your code here.
L = [0 for _ in range(len(A)+1)]
R = [0 for _ in range(len(A)+1)]

for i in range(len(A)):
    if A[i] == '(':
        L[i+1] = L[i] + 1
    else:
        L[i+1] = L[i]
for i in range(len(A)-1,-1,-1):
    if A[i] == ')':
        R[i] = R[i+1] + 1
    else:
        R[i] = R[i+1]
answer = 0
for i in range(1,len(A)):
    answer = max(answer, min(L[i],R[i]))
print(answer)