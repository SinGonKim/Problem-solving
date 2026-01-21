from bisect import bisect_left

# Please write your code here.
def main():
    ans = 0
    for left_idx, small_num in enumerate(arr):
        if small_num >= k: break
        large_num = k - small_num
        right_idx = bisect_left(arr, large_num)
        if right_idx - left_idx <= 0:break
        ans += right_idx - left_idx
    return ans

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = sorted([int(input()) for _ in range(n)])
    ans = main()
    print(ans)
