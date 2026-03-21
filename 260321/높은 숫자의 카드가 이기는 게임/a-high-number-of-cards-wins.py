n = int(input())

a_cards = []
b_cards = [int(input()) for _ in range(n)]

b_set = set(b_cards)

a_cards = [num for num in range(1, 2*n+1) if num not in b_set]

a_cards.sort()
b_cards.sort()

ans = 0
b_idx = 0

for a_idx in range(n):
    if b_idx < n and a_cards[a_idx] > b_cards[b_idx]:
        ans += 1
        b_idx += 1
print(ans)