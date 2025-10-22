m = int(input())
a, b = map(int, input().split())

# Please write your code here.

import sys
min_cnt = sys.maxsize
max_cnt = -sys.maxsize

def binary_search(target_num):
    left = 1
    right = m
    cnt = 0

    while left <= right:
        cnt += 1

        mid = (left + right)//2

        if mid == target_num:
            return cnt
        
        if mid > target_num:
            right = mid - 1
        else:
            left = mid + 1
    return cnt


while a<= b:
    target_num = a
    cnt = binary_search(target_num)
    max_cnt = max(cnt, max_cnt)
    min_cnt = min(cnt, min_cnt)
    a += 1
print(min_cnt, max_cnt)