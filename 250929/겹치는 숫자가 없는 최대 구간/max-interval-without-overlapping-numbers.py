n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
count_array = [0]*100001
answer = 0
j = 0
for i in range(n):
    while j < n and count_array[arr[j]] != 1:
        count_array[arr[j]] += 1
        j += 1
    
    answer = max(answer, j-i)

    count_array[arr[i]] -= 1

print(answer)