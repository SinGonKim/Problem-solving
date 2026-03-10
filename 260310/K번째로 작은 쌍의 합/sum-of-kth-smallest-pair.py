import heapq

n, m, k = map(int, input().split())
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())))


# heap 원소: (합, arr1의 인덱스 i, arr2의 인덱스 j)
heap = []

# 시작 상태: 각 arr1[i]와 arr2[0]의 조합
for i in range(n):
    heapq.heappush(heap, (arr1[i] + arr2[0], i, 0))

answer = 0

for _ in range(k):
    answer, i, j = heapq.heappop(heap)
    
    # 같은 arr1[i]에 대해 arr2의 다음 원소를 붙인 쌍 추가
    if j + 1 < m:
        heapq.heappush(heap, (arr1[i] + arr2[j + 1], i, j + 1))

print(answer)