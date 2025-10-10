n, k = map(int, input().split())
bomb_list = [int(input()) for _ in range(n)]

# 함수들
# is_about_to_blow_up(curr_idx)
def is_about_to_blow_up(curr_idx):
    
    # curr_bomb_num
    curr_bomb_num = bomb_list[curr_idx]

    # curr_idx이후부터 k번 후까지 탐색
    for i in range(curr_idx+1, curr_idx + k + 1):
        # 같은 번호의 폭탄이 있으면,
        if bomb_list[i] == curr_bomb_num:
            # 터짐
            return True
    return False

# get_bomb_nums_and_num(curr_idx)
def get_bomb_nums_and_num(curr_idx):

    # curr_bomb_num
    curr_bomb_num = bomb_list[curr_idx]

    # curr_bomb_nums
    curr_bomb_nums = 0

    # curr_idx부터 k번 후까지 탐색
    for i in range(curr_idx, curr_idx + k + 1):
        # 같은 번호의 폭탄이 있으면,
        if bomb_list[i] == curr_bomb_num:
            # curr_bomb_nums 올려주기
            curr_bomb_nums += 1
    
    # 터질 폭탄의 개수와
    # 폭탄의 번호를 tuple 형태로 반환
    return (curr_bomb_nums, curr_bomb_num)

bombs_about_to_blow_up = []

for i in range(n - k):
    if is_about_to_blow_up(i):
        bombs_about_to_blow_up.append(get_bomb_nums_and_num(i))

bombs_about_to_blow_up.sort()

if not bombs_about_to_blow_up:
    print(-1)
else:
    bomb_nums, bomb_num = bombs_about_to_blow_up[-1]
    print(bomb_num)