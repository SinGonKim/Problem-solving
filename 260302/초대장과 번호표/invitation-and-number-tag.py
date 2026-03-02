N, G = map(int, input().split()) # 사람 수, 그룹 수

group = []
group_size = []

for _ in range(G):
    nums = list(map(int, input().split()))
    group_size.append(nums[0])
    group.append(nums[1:])

# Please write your code here.
p = set()
p.add(1)

while True:
    tmp = []
    tmp_size = []
    if len(group) == 0: break

    for idx, g in enumerate(group):
        if group_size[idx] == 0: continue
        cnt = 0
        res = []
        for num in g:
            if num in p:
                cnt += 1
            else:
                res.append(num)
        if cnt == group_size[idx] - 1:
            p.add(res[0])
        else:
            tmp.append(res)
            tmp_size.append(len(res))
    if len(tmp_size) == len(group_size):
        break
    else:
        group_size = tmp_size
        group = tmp
print(len(p))


    
