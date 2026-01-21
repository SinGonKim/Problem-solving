MAX_INDEX = 4_000_001
n, k = map(int, input().split())
candies = [(-1,-1)]
for _ in range(n):
    cnt, x = tuple(map(int, input().split()))
    candies.append((x,cnt))

def get_pos_of_candy(candy_idx):
    x, _ = candies[candy_idx]
    return x

def get_num_of_candy(candy_idx):
    _ ,cnt = candies[candy_idx]
    return cnt

candies.sort()
ans = 0
total_nums = 0
j = 0
for i in range(1,n + 1):
    while j + 1 <= n and get_pos_of_candy(j+1) - get_pos_of_candy(i) <= 2*k:
        total_nums += get_num_of_candy(j+1)
        j += 1
    ans = max(ans, total_nums)

    total_nums -= get_num_of_candy(i)
print(ans)