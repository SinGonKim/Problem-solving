N = int(input())
a = input()
b = input()

# Please write your code here.

diff = []
for i in range(N):
    if a[i] != b[i]:
        diff.append(1)
    else:
        diff.append(0)

flip_count = 0
in_group = False

for i in range(N):
    if diff[i] == 1:
        if not in_group:
            flip_count += 1
            in_group = True
    else:
        in_group = False

print(flip_count)
