from collections import defaultdict
def get_xor(arr):
    result = 0
    for i in range(len(arr)):
        if i == 0:
            result = nums[arr[i]]
        else:
            result = nums[arr[i]] ^ result

    return result


def choose(idx):
    global max_xor
    if idx == M + 1:

        # xor 계산
        xor = get_xor(arr)

        if xor > max_xor:
            max_xor = xor

        return


    for i in range(1, N + 1):

        if not visited[i]:

            # memoization
            temp = arr[:]
            temp.append(i)
            key = tuple(sorted(temp))

            if memo[key] == 1:
                continue
            memo[key] = 1

            visited[i] = True

            arr.append(i)
            choose(idx + 1)
            arr.pop()

            visited[i] = False


if __name__ == "__main__":
    N, M = map(int, input().split())


    nums = [0] + list(map(int, input().split()))

    if M == 1:
        print(max(nums))

    else:
        
        max_xor = 0

        arr = []
        memo = defaultdict(int)

        visited = [True] + [False] * N

        choose(1)
        print(max_xor)