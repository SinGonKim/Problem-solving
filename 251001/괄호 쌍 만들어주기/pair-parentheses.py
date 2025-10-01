A = input()

# Please write your code here.
n = len(A)
open_count = 0  # 지금까지 발견한 '(('의 개수
total_pairs = 0  # 총 쌍의 개수

# 모든 가능한 '((' 위치를 찾기
for i in range(n - 1):
    if A[i] == '(' and A[i + 1] == '(':
        open_count += 1
    elif A[i] == ')' and A[i + 1] == ')':
        total_pairs+= open_count
print(total_pairs)