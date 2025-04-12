from itertools import combinations

def get_max_xor(nums, M):
    max_xor = 0
    for comb in combinations(nums, M):
        xor = 0
        for num in comb:
            xor ^= num
        max_xor = max(max_xor, xor)
    return max_xor

if __name__ == "__main__":
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    if M == 1:
        print(max(nums))
    else:
        print(get_max_xor(nums, M))
