temp = input()
input_str = "#" + "#".join(list(temp)) + "#"
n = len(input_str)
# Please write your code here.
A = [0 for _ in range(n)]
r, p = -1, -1

for i in range(n):
    if r < i:
        A[i] = 0
    else:
        ii = 2*p - i
        A[i] = min(r-i, A[ii])
    
    while i - A[i] - 1 >= 0 and i + A[i] + 1 < n and input_str[i-A[i]-1] == input_str[i+A[i]+1]:
        A[i] += 1
    
    if i + A[i] > r:
        r, p = i + A[i], i
ans = 0
for i in range(n):
    ans = max(ans ,2*A[i]+1)
print(ans//2)
