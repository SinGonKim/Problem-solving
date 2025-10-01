A = input()

# Please write your code here.
n = len(A)
count = 0

# 모든 가능한 '((' 위치를 찾기
for i in range(n - 1):
    if A[i] == '(' and A[i + 1] == '(':
        # 이 '((' 뒤에 있는 모든 '))'를 찾기
        for j in range(i + 2, n - 1):
            if A[j] == ')' and A[j + 1] == ')':
                count += 1
print(count)