n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()

idx = n
import sys
answer = sys.maxsize
for k in range(idx):
    answer = min(answer, abs(arr[idx+k] - arr[k]))
print(answer)